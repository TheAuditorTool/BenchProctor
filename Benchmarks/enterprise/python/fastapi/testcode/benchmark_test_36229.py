# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import base64
import urllib.request
import urllib.parse
import ssl
from app_runtime import db


async def BenchmarkTest36229(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = base64.b64decode(db_value).decode('utf-8', 'ignore')
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return {"updated": True}
