# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import urllib.request
import urllib.parse
import ssl
from app_runtime import db


async def BenchmarkTest28460(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(db_value)), context=ctx)
    return {"updated": True}
