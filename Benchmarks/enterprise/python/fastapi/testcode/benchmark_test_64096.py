# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import urllib.request
from app_runtime import db


async def BenchmarkTest64096(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    if db_value not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = db_value
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(processed)).read()
    return {"updated": True}
