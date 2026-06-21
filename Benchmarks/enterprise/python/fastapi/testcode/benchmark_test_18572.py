# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import urllib.request
import urllib.parse
import ssl
from app_runtime import db


async def BenchmarkTest18572(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    pending = list(str(comment_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return {"updated": True}
