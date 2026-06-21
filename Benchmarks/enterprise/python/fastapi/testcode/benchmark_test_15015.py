# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from starlette.responses import JSONResponse
import hashlib
from app_runtime import db


request_state: dict[str, str] = {}

async def BenchmarkTest15015(request: Request):
    referer_value = request.headers.get('referer', '')
    request_state['last_input'] = referer_value
    data = request_state['last_input']
    _resp = requests.get(str(data))
    if hashlib.sha256(_resp.content).hexdigest() != _resp.headers.get('X-Content-SHA256'):
        return JSONResponse({'error': 'integrity check failed'}, status_code=502)
    db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return {"updated": True}
