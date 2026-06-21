# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse
import urllib.request
from app_runtime import db


async def BenchmarkTest78771(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', db_value):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = db_value
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(processed)).read()
    return {"updated": True}
