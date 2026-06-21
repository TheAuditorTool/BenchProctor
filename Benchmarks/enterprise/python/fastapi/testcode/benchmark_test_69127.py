# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import json
from starlette.responses import JSONResponse
import hashlib
from app_runtime import db


async def BenchmarkTest69127(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    _resp = requests.get(str(data))
    if hashlib.sha256(_resp.content).hexdigest() != _resp.headers.get('X-Content-SHA256'):
        return JSONResponse({'error': 'integrity check failed'}, status_code=502)
    db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return {"updated": True}
