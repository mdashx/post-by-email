"""
This is a scratch file for creating tests during development
"""

import pytest

from post_by_email.get_emails import get_emails
from post_by_email.version_commands import pull_changes, push_changes


@pytest.mark.skipif(
    True,
    reason="Just for use during development, depends on live connection to server.",
)
def test_get_emails():
    emails = get_emails()
    for email in emails:
        print(email)


@pytest.mark.skipif(
    True,
    reason="Just for use during development, depends on live connection to server.",
)
def test_pull_changes():
    pull_changes()


@pytest.mark.skipif(
    True,
    reason="Just for use during development, depends on live connection to server.",
)
def test_push_changes():
    push_changes()


email1 = {
    "date": "2021-09-20",
    "title": "Blog v2 Intro",
    "body": '\n\nThis is blog v2, although it\'s at least my 4th blog that I can remember...\n\n1. On my first homepage\n2. Programming blog, "The Well-shorn Yak" on Blog Spot or whatever it was\n3. My first blog on MDashX\n4. This blog\n\nThe contents of 1 and 2 are unfortunately lost. The best thing I got out of those was when I wrote an article on how to modify the Flask source code to make it work with JSONP. If I were smarter I would\'ve actually contributed the code to Flask, but anyway people were looking for the solution and my blog was the top search result on the topic back in the day (this was around 2011-2012). It was a small thing, but it was really nice when people thanked me for writing the article.\n\nThe contents of number 3 are mixed into the "notes" section of this site.\n\nThere is no point to this blog other than to be as bloggy as possible, with unchecked drivel, personal trivia and over-sharing, repetition of tired cliches, and most likely going dark for long-periods with no explanation.\n',
}

email2 = {
    "date": "2021-09-20",
    "title": "Blog - haskell",
    "body": "\n\nA long time ago I subscribed to email notifications from Bartosz Milewski's blog. The last notification I received kicked off some potential energy that's been building up for years, waiting for the right time.\n\nSo now I'm watching lectures on category theory and working through a book on Haskell.\n\nI've learned a little Haskell on and off over the years. The result so far is that when I'm writing Python or JavaScript I use first-class functions and closures as easily as I use print statements.\n\nI'm always messing around with different languages that I find interesting. APL is one of my favorites for when I just having fun learning something new. But I think there is a future with Haskell and at the moment I'm committed to gaining actual competence with the language.\n\n\n\n\n\n",
}
