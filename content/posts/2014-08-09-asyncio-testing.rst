=====================================
Twisted-like unit testing for asyncio
=====================================

:date: 2015-08-09
:category: development
:tags: asyncio, python, twisted, testing, unittest
:status: draft

Recently I've been porting some code for a personal project from `Twisted
<https://twistedmatrix.com/>`_ to the python3 builtin `asyncio
<https://docs.python.org/3/library/asyncio.html>`_ library. The change is not
as drastic as it might seem, since the two libraries share the same basic
concepts (using different names, e.g. Future vs Deferred, loop vs reactor) and
the asyncio design is quite inspired by Twisted's.

One thing I found is that adapting the code was actually easier and quicker
than changing unit tests.

Testing asynchronous code requires some setup, like managing the event loop,
creating callback chains to assert on results from asynchronous methods.
Twisted provides very nice facilities for this, which eliminate some of the
setup boilerplate and make test clearer to read and more concise.

Its ``trial`` test runner automatically manages setting up, starting and
stopping the reactor, and handles waiting for a ``Deferred`` when a test method
returns one.  This makes it possible to add callbacks to it, that assert on the
result of the asynchronous call. For example:

.. code-block:: python

  def test_async_call(self):
      deferred = call_under_test()
  
      def check(result):
          self.assertEqual(result, 19)
  
      return deferred.addCallback(check)

will run the ``check`` callback when the deferred yields its result.
The same can be written more concisely using ``@inlineCallbacks``:
      
.. code-block:: python

  @inlineCallbacks
  def test_async_call(self):
      result = yield call_under_test()
      self.assertEqual(result, 19)

which comes especially handy when multiple asynchronous calls are unsed in a
single test (so you don't need to chain a lot of callbacks).

While moving my code to asyncio, I wanted to keep the same unit test style, but
unfortunately I didn't find much builtin support for it.  Looking at tests for
libraries using asyncio, I noticed most of them deal with the event loop
directly, running the method under test under it:


.. code-block:: python

  def test_async_call(self):
      loop = asyncio.get_event_loop()
      result = loop.run_until_complete(call_under_test())
      self.assertEqual(result, 19)


That's fine if you're testing a single call, but it gets cumbersome
when you have multiple calls, possibly with depending on the result of the
previous one.

Luckily, it wasn't to hard to implement a test behavior like the one provided
by Twisted with asyncio, so I created a `LoopTestCase
<https://bitbucket.org/ack/toolrack/src/b8666d467a18b94338b6792dbe8dd4d6a6e3a7ba/toolrack/testing/async.py?at=master>`_
which provides an event loop (derived from ``asyncio.test_utils.TestLoop``)
which wraps test methods so that if they return a ``Future`` or are coroutines,
the loop is run until they complete.

So the test case above simply becomes something like:

.. code-block:: python

  def test_async_call(self):
      result = yield from call_under_test()
      self.assertEqual(result, 19)

Notice that there's no need to decorate the method as ``@coroutine`` (like with
Twited's ``@inlineCallbacks``).


Controlling time
----------------

Both Twisted and asyncio provide methods scheduling function calls at a certain
time, or after a time delta. Testing code that use these functionalities
requires to be able to manipulate the event loop time manually, to avoid having
tests to actually wait for time to pass.  Twisted provides
``twisted.internet.task.Clock`` which behaves like the reactor, but provides an
``advance()`` method to move the time forward.

.. code-block:: python

  def test_call_later(self):
      calls = []
      clock = Clock()
      clock.callLater(5, calls.append, True)
      self.assertEqual([], calls)
      clock.advance(5)
      self.assertEqual([True], calls)

The ``asyncio.test_utils.TestLoop`` also provides an ``advance_time()`` method,
but this just moves the time forwards, so you still need to manually schedule
an event loop run to cause the scheduled function to be called.

So I enhanced the ``TestLoop`` used by ``LoopTestCase`` to do this
automatically, via the ``advance()`` method.  With this change, the previous
tests looks pretty much the same with asyncio:

.. code-block:: python

  def test_call_later(self):
      calls = []
      self.loop.call_later(5, calls.append, True)
      self.assertEqual([], calls)
      self.loop.advance(5)
  self.assertEqual([True], calls)

For a more meaningful example, let's use Twisted ``LoopingCall``, which
periodically runs the passed function:

.. code-block:: python

  def test_periodic(self):
      calls = []
      call = LoopingCall(calls.append, True)
      clock = Clock()
      call.clock = clock  # use the test clock instead of the reactor

      call.start(5)
      self.assertEqual(calls, [True])
      clock.advance(5)
      self.assertEqual(calls, [True, True])
      clock.advance(5)
      self.assertEqual(calls, [True, True, True])

and the corresponding asyncio code:

.. code-block:: python

  def test_periodic(self):
      calls = []
      call = PeriodicCall(self.loop, calls.append, True)

      call.start(5)
      self.assertEqual(calls, [True])
      self.loop.advance(5)
      self.assertEqual(calls, [True, True])
      self.loop.advance(5)
      self.assertEqual(calls, [True, True, True])

where ``PeriodicCall`` (again from my `ToolRack
<https://bitbucket.org/ack/toolrack>`_ library) is basically a port of
``LoopingCall`` to asyncio.
