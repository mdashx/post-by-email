from post_by_email.create_post import title_to_slug, create_doc


def test_title_to_slug():
    cases = [
        ("I am a title", "i-am-a-title"),
        ("Number 5", "number-5"),
        ("Cat's cradle", "cats-cradle"),
        ("Enemy of the state Ⓐ", "enemy-of-the-state"),
        ("   Too  many  spaces  Ⓐ", "too-many-spaces"),
    ]
    for case in cases:
        assert title_to_slug(case[0]) == case[1]


def test_create_doc():
    email1 = {
        "date": "2021-09-20",
        "title": "Title One",
        "body": "\n\nI am the first blog post.\n\n\n",
    }

    email2 = {
        "date": "2021-09-20",
        "title": "Article Two",
        "body": "I am the second blog post.\n\nLook at me go.",
    }

    doc1 = """{
  "title": "Title One",
  "publishdate": "2021-09-20"
}

I am the first blog post."""

    doc2 = """{
  "title": "Article Two",
  "publishdate": "2021-09-20"
}

I am the second blog post.

Look at me go."""

    assert create_doc(email1) == doc1
    assert create_doc(email2) == doc2
