#!/bin/bash

#echo -e "Content-type: text/html\n\n"
#cat <<EOF
#<html>
#<body>
#EOF

#echo "<pre>Request Method = $REQUEST_METHOD</pre>"
#echo "<pre>Content Type = $CONTENT_TYPE</pre>"
#echo "<pre>Content Length = $CONTENT_LENGTH</pre>"
#echo "<pre>Query String = $QUERY_STRING</pre>"

BODY_TEXT=$(echo "${QUERY_STRING}" | tr "&" "\n")
#echo "<pre>body text = "${BODY_TEXT}"</pre>"

#cat <<EOF
#</body>
#</html>
#EOF

# Replace non-useful query string items with blankness.
BODY_TEXT="${BODY_TEXT/Submit=Submit/''}"
BODY_TEXT="${BODY_TEXT/_nof_param_file=FormInfo_LAYOUTFORM_Layout_13704.XML/''}"

# URL decode
#local url_encoded="${1//+/ }"
#printf '%b' "${url_encoded//%/\\x}"

# Send email with ssmtp
cat <<EOF | ssmtp jody@kaplon.us
To: jody@kaplon.us
From: alertmonitorfl@gmail.com
Subject: pc-warrants contact

"${BODY_TEXT}"
EOF

cat <<EOF
Status: 302 Found
Location: ./Reply_Page/reply_page.html


EOF
