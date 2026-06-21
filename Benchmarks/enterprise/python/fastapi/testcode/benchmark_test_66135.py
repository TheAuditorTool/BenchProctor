# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import urllib.request
from app_runtime import db


async def BenchmarkTest66135(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = '{}'.format(db_value)
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return {"updated": True}
