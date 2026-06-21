# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import urllib.request
from app_runtime import db


async def BenchmarkTest41760(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(comment_value)
    data = collected
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return {"updated": True}
