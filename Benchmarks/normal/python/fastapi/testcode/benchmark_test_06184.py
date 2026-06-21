# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
import json
from pydantic import BaseModel
from starlette.responses import JSONResponse


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest06184(request: Request, req: UserInput):
    json_value = req.payload
    data = json.loads(json_value).get('value', '')
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
