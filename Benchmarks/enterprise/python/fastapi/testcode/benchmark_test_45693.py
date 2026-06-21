# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import urllib.request
from app_runtime import db


async def BenchmarkTest45693(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    if comment_value:
        data = comment_value
    else:
        data = ''
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return {"updated": True}
