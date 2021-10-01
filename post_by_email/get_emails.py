"""
IMAP SEARCH: https://datatracker.ietf.org/doc/html/rfc3501#section-6.4.4

IMAP FETCH: https://datatracker.ietf.org/doc/html/rfc3501#section-6.4.5

From https://docs.python.org/3/library/imaplib.html#imap4-objects: 

>The message_set options to commands below is a string specifying one
> or more messages to be acted upon. It may be a simple message number
> ('1'), a range of message numbers ('2:4'), or a group of
> non-contiguous ranges separated by commas ('1:3,6:9'). A range can
> contain an asterisk to indicate an infinite upper bound ('3:*').

...can also be a list of numbers like this: '1,3,5'

"""

import email.utils
from imaplib import IMAP4_SSL

import post_by_email.settings as settings

EMAIL_HOST = settings.EMAIL_HOST
EMAIL_USER = settings.EMAIL_USER
EMAIL_PASS = settings.EMAIL_PASS
EMAIL_RECIPIENT = settings.EMAIL_RECIPIENT
APPROVED_SENDER = settings.APPROVED_SENDER


def parse_headers(headers):
    title = headers.split("Subject:")[1].strip()
    publish_date = headers.split("Subject:")[0].split("Date:")[1].strip()
    publish_date = email.utils.parsedate_to_datetime(publish_date)
    publish_date = publish_date.strftime("%Y-%m-%d")
    return title, publish_date


def parse_body(body):
    body = body.split("Content-Type: text/html")[0]
    body = body.split("Content-Type: text/plain")
    body = body[1]

    # The last line of body now has leftover junk that was part of
    # the HTML content, so we remove the last line.
    body = body.splitlines()
    body = "\n".join(body[:-1])
    return body


def get_emails():
    conn = IMAP4_SSL(host=EMAIL_HOST)
    conn.login(EMAIL_USER, EMAIL_PASS)
    conn.select("INBOX")
    response_code, msg_nums = conn.search(
        None, f"TO {EMAIL_RECIPIENT} FROM {APPROVED_SENDER}"
    )
    msg_nums = msg_nums[0].decode("utf-8").split()

    for msg_num in msg_nums:
        response_code, header_response = conn.fetch(
            msg_num, "BODY[HEADER.FIELDS (DATE SUBJECT)]"
        )
        response_code, body_response = conn.fetch(msg_num, "BODY[TEXT]")

        headers = header_response[0][1].decode("utf8")
        body = body_response[0][1].decode("utf8")

        yield {"headers": headers, "body": body}

    conn.close()
    conn.logout()
