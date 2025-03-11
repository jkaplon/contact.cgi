Bash script to send emails based on web contact form submissions.
This script replaced a hideously long/complicated PHP script behind a static website.
I was asked to move the site to a new VPS when the previous host was taken over by spammers.
I've never proved it, but I *think* that PHP script might have been how the spammers got into the original VPS.

Use of the `ssmtp` mail program to send via gmail has been a good alternative to running a full email server.
Gmail setup for this is frustratingly different each time, but should remain possible as long as google continues to allow app-specific passwords.
On other projects I've used email forwarding services like [forwardemail.net](https://forwardemail.net).

I planned to add validations for empty or spammy submissions along with rate-limiting, but they were never needed.
