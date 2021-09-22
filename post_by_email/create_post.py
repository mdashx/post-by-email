"""This code only adds posts to a single path on the site. Sorry!
"""

import json
import os
import re

import post_by_email.settings as settings


def title_to_slug(title):
    """title should be a string, this function turns it into a slug and
    returns the slug as a string.
    """
    title = title.strip()
    title = title.lower()
    title = title.replace(" ", "-")
    nonalpha = re.compile(r"[^a-zA-Z0-9_-]")
    title = nonalpha.sub("", title)
    title = title.replace("--", "-")
    title = title.strip("-")

    return title


def create_doc(email):
    """email is a dict with the fields 'date', 'title' and 'body'

    We will put date and title into JSON front-matter, which will have
    hardcoded keys for now to match my blog, but can be made more
    flexible in the future, and we will put the body text underneath
    the JSON.

    This entire doc will be returned, ready to save on the filesystem
    with a '.md' extension.
    """

    doc = ""

    frontmatter = json.dumps(
        {
            "title": email["title"],
            "publishdate": email["date"],
        },
        indent=2,
    )

    doc = doc + frontmatter
    doc = doc + "\n\n"
    doc = doc + email["body"].strip()
    return doc


def save_doc(slug, doc):
    filename = f"{slug}.md"
    with open(os.path.join(settings.CONTENT_PATH, filename), "w") as fh:
        fh.write(doc)
