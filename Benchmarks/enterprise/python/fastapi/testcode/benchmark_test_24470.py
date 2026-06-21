# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from pydantic import BaseModel
from starlette.responses import JSONResponse


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest24470(request: Request, req: UserInput):
    json_value = req.payload
    data = (lambda v: v.strip())(json_value)
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
