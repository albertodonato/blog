========================
Tracking Launchpad karma
========================

:date: 2015-10-16
:category: misc
:tags: python, launchpad

Launchpad_ tracks how active a user is by assigning points to each activity
that is performed, such as working with branches, managing bugs, packaging
(uploading to PPAs), merge proposals. This resulting score constitutes the user
"Karma_".

Since I use Launchpad on a daily basis, I was curious about how my Karma varies
over time; unfortunately Launchpad doesn't have a way of doing this, since it
only reports the current value.

So I thought it'd be nice to have a simple script to collect the Karma value on
a daily basis (the value is not updated in real time in Launchpad so there's no
value in collecting it more frequently).

Of course getting the data is only half of the story, the fun part is actually
building some nice graphs. So, after having a first version of the script
running for a while and just collecting data in a SQLite database, I finally
got some time to extend it to also generate a page with graphs. You can see the
result `here <https://albertodonato.net/launchpad-karma>`_.

If you want to track your own Karma, the script is available on Bitbucket_; it
is trivial to set up and run daily via ``cron``. By default, it both fetches
the current value (storing it into the database) and regenerate the graph
page. Just make the target directory available via static file serve on your
web server and you're all set.


.. _Launchpad: https://launchpad.net/
.. _Karma: https://help.launchpad.net/YourAccount/Karma
.. _Bitbucket: https://bitbucket.org/ack/launchpad-karma
