#!/bin/bash

urldecode() {
    # urldecode <string>

    local url_encoded="${1//+/ }"
    # Hack to replace user-enterd ampersand w/full word, makes formatting easier later in script.
    url_encoded="${url_encoded//%26/' and '}"
    printf '%b' "${url_encoded//%/\\x}"
}

BODY_TEXT="$(urldecode $QUERY_STRING)"

# Relies on previous hack to replace user-enterd ampersands.
BODY_TEXT=$(echo "${BODY_TEXT}" | tr "&" "\n")

# Replace non-useful query string items with blankness.
BODY_TEXT="${BODY_TEXT/Submit=Submit/''}"
BODY_TEXT="${BODY_TEXT/_nof_param_file=FormInfo_LAYOUTFORM_Layout_13704.XML/''}"
BODY_TEXT="${BODY_TEXT/email=/''}"

# Send email with ssmtp
cat <<EOF | ssmtp recipient@example.com
To: recipient@example.com
From: alertmonitorfl@gmail.com
Subject: pc-warrants contact

${BODY_TEXT}
EOF

cat <<EOF
Status: 302 Found
Location: ./Reply_Page/reply_page.html


EOF
