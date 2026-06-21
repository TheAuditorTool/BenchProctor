# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from starlette.responses import JSONResponse
import hashlib
from app_runtime import db


async def BenchmarkTest54596(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    _resp = requests.get(str(xml_value))
    if hashlib.sha256(_resp.content).hexdigest() != _resp.headers.get('X-Content-SHA256'):
        return JSONResponse({'error': 'integrity check failed'}, status_code=502)
    db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return {"updated": True}
