# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import urllib.request
from app_runtime import db


async def BenchmarkTest39739(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(comment_value)).read()
    return {"updated": True}
