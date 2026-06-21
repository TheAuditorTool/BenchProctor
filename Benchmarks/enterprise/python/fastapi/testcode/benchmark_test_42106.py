# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from pydantic import BaseModel
from starlette.responses import JSONResponse


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest42106(request: Request, req: UserInput):
    json_value = req.payload
    prefix = ''
    data = prefix + str(json_value)
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
