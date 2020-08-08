#!/usr/bin/env python
import os
import sys

mandatory_env_vars = [
    "TWITTER_CONSUMER_KEY",
    "TWITTER_CONSUMER_SECRET",
    "TWITTER_ACCESS_TOKEN",
    "TWITTER_ACCESS_TOKEN_SECRET",
]
missing = False

for var in mandatory_env_vars:
    if var not in os.environ or os.environ[var] == "none":
        print(f"{var} is required", sys.stderr)
        missing = True

if missing:
    exit(1)

TWITTER_CONSUMER_KEY = os.environ.get("TWITTER_CONSUMER_KEY")
TWITTER_CONSUMER_SECRET = os.environ.get("TWITTER_CONSUMER_SECRET")
TWITTER_ACCESS_TOKEN = os.environ.get("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")

PORT = os.environ.get("PORT", "8000")
