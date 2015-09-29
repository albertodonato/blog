==============
HTTP/2-enabled
==============

:date: 2015-09-29
:category: web
:tags: news, http2
:summary: This blog is now served with HTTP/2...

This blog is now served on HTTP/2. It's powered by `nginx 1.9.5
<http://nginx.org>`_, which includes experimental support for the protocol.

Enabling HTTP/2 support in nginx is just a matter of adding the ``http2`` option
to the ``listen`` directive:

.. code-block:: nginx

  listen 443 ssl http2;
  listen [::]:443 ssl http2;


Previously, I've been using the ``spdy`` option to enable the (also
experimental) `SPDY/3.1 <https://www.chromium.org/spdy/spdy-whitepaper>`_
support. From version 1.9.5, this option is superseded in favor of the
``http2`` one.
