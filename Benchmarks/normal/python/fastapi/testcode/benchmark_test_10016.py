# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse
import urllib.request
from types import SimpleNamespace
from app_runtime import db


async def BenchmarkTest10016(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    ns = SimpleNamespace(payload=db_value)
    data = getattr(ns, 'payload')
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(processed)).read()
    return {"updated": True}
