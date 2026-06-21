# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest62756(request: Request, req: UserInput):
    json_value = req.payload
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(json_value), secure=True, httponly=True, samesite='Strict')
    return resp
