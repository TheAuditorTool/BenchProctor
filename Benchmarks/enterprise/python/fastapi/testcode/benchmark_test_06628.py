# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from pydantic import BaseModel
from starlette.responses import JSONResponse
import hashlib
from app_runtime import db


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest06628(request: Request, req: UserInput):
    json_value = req.payload
    data = json_value if json_value else 'default'
    _resp = requests.get(str(data))
    if hashlib.sha256(_resp.content).hexdigest() != _resp.headers.get('X-Content-SHA256'):
        return JSONResponse({'error': 'integrity check failed'}, status_code=502)
    db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return {"updated": True}
