# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from dataclasses import dataclass
from starlette.responses import JSONResponse
import hashlib
from app_runtime import db


@dataclass
class FormData:
    payload: str

async def BenchmarkTest25623(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = FormData(payload=forwarded_ip).payload
    _resp = requests.get(str(data))
    if hashlib.sha256(_resp.content).hexdigest() != _resp.headers.get('X-Content-SHA256'):
        return JSONResponse({'error': 'integrity check failed'}, status_code=502)
    db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return {"updated": True}
