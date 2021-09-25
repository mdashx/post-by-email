from post_by_email.get_emails import extract_headers


def test_extract_headers():
    headers1 = """Date: Sat, 25 Sep 2021 13:07:24 -0600
Subject: A much better test post"""

    date, subject = extract_headers(headers1)

    assert date == "2021-09-25"
    assert subject == "A much better test post"
