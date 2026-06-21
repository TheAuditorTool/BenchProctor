# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import urllib.request
from app_runtime import db


async def BenchmarkTest11430(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    prefix = ''
    data = prefix + str(db_value)
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return {"updated": True}
