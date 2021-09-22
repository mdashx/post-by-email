"""This module expects an SSH clone of an upstream Git repo to exist
at the PROJECT_PATH and the SSH key to be avilable in the shell.

New posts are added to the master branch.

If you have local changes or anything else that stops your repo from
pulling from master, then this code may not work. This code is
designed to work with a repo where users are not also making manual
changes, i.e. on a server that builds the site from emails and does
not have users editing the site there as well.
"""

import os
import subprocess

import post_by_email.settings as settings


def pull_changes():
    os.chdir(settings.PROJECT_PATH)
    subprocess.run(["git", "checkout", "master"])
    subprocess.run(["git", "pull", "origin", "master"])


def push_changes():
    os.chdir(settings.PROJECT_PATH)
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "Auto-committed by 'post_by_email'"])
    subprocess.run(["git", "push", "origin", "master"])


def deploy():
    """Sorry, this deploy command is really specific to my blog"""
    os.chdir(settings.PROJECT_PATH)
    subprocess.run(
        [
            "make",
            "deploy",
            f"USER={settings.USER}",
            f"HOST={settings.HOST}",
            f"WORKING_DIR={settings.WORKING_DIR}",
            f"HOST_DOMAIN={settings.HOST_DOMAIN}",
        ]
    )
