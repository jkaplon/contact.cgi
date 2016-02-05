I hacked together this bash script to handle contact form submissions on a friend's website.
The contact form was previoulsy using a hideously long and complex PHP script, which I wanted to avoid.
I've never proved it, but I blame that PHP script for my frirend's previous webserver getting taken over by spammers.
Also, if possible, I wanted to avoid the overhead of running a full email server.

This script and the `ssmtp` mail program have proven to be a good solution for me.
Bash scripting is not a frequent task for me, so this script could probably benefit from some refactoring (to add environment variables, for example).
There are also some brittle website-specific values, but at least there are comments!
