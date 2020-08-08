#!/usr/bin/env python
from twitterss.core import app
from twitterss import settings

if __name__ == "__main__":
    app.run(port=int(settings.port))
