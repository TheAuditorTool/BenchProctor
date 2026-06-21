# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
import json
from pydantic import BaseModel
from starlette.responses import JSONResponse
import os


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest48131(request: Request, req: UserInput):
    json_value = req.payload
    data = json.loads(json_value).get('value', '')
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
