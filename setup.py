import os
from setuptools import find_packages, setup

POST_BY_EMAIL_VERSION = os.getenv("POST_BY_EMAIL_VERSION", "0.1-rc1")

setup(
    name="post_by_email",
    version=POST_BY_EMAIL_VERSION,
    description="Post to Hugo via email",
    include_package_data=True,
    packages=find_packages(exclude=["contrib", "docs", "tests"]),
    install_requires=[
        "python-dotenv",
    ],
)
