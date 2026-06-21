# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import urllib.request
import urllib.parse
import ssl
from app_runtime import db


async def BenchmarkTest36660(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = json.loads(db_value).get('value', '')
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_OPTIONAL
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return {"updated": True}
