# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from pydantic import BaseModel
from starlette.responses import JSONResponse


class UserInput(BaseModel):
    payload: str = ''
def relay_value(value):
    return value

async def BenchmarkTest01522(request: Request, req: UserInput):
    json_value = req.payload
    data = relay_value(json_value)
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
