from post_by_email.get_emails import parse_body, parse_headers


def test_parse_headers():
    headers = """Date: Fri, 01 Oct 2021 12:43:13 -0600
Subject: Test post for refactoring"""
    expected_title = "Test post for refactoring"
    expected_date = "2021-10-01"
    title, date = parse_headers(headers)
    assert expected_title == title
    assert expected_date == date


def test_parse_body():
    email_body = """--0ba5d8c65e3d45de8681af61c66ddbe7
Content-Type: text/plain

I am a post to use for testing and refactoring.
--0ba5d8c65e3d45de8681af61c66ddbe7
Content-Type: text/html

<!DOCTYPE html><html><head><title></title><style type="text/css">p.MsoNormal,p.MsoNoSpacing{margin:0}
p.MsoNormal,p.MsoNoSpacing{margin:0}</style></head><body><div>I am a post to use for testing and refactoring.<br></div></body></html>
--0ba5d8c65e3d45de8681af61c66ddbe7--"""

    post_body = "\n\nI am a post to use for testing and refactoring."
    assert parse_body(email_body) == post_body
