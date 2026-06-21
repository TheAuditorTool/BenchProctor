# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import urllib.request
from app_runtime import db


async def BenchmarkTest67211(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        data = json.loads(comment_value).get('value', comment_value)
    except (json.JSONDecodeError, AttributeError):
        data = comment_value
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return {"updated": True}
