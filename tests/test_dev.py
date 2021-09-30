"""
This is a scratch file for creating tests during development
"""

import pytest

from post_by_email.get_emails import get_emails
from post_by_email.version_commands import deploy, pull_changes, push_changes
from post_by_email.create_post import save_doc


@pytest.mark.skipif(True, reason="for dev")
def test_get_emails():
    emails = get_emails()
    for email in emails:
        print(email)


@pytest.mark.skipif(True, reason="for dev")
def test_pull_changes():
    pull_changes()


@pytest.mark.skipif(True, reason="for dev")
def test_push_changes():
    push_changes()


@pytest.mark.skipif(True, reason="for dev")
def test_save_doc():
    slug = "just-a-test"
    doc = "I am a test document"
    save_doc(slug, doc)


@pytest.mark.skipif(True, reason="for dev")
def test_deploy():
    deploy()
