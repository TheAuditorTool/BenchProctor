# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
import json
from pydantic import BaseModel
from starlette.responses import JSONResponse


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest49543(request: Request, req: UserInput):
    json_value = req.payload
    data = json.loads(json_value).get('value', '')
    digest = hashlib.sha256(('static_salt_123' + str(data)).encode()).hexdigest()
    return JSONResponse({'digest': str(digest)}, status_code=200)
