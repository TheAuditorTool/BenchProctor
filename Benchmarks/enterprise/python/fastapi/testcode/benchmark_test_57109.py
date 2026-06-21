# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''
request_state: dict[str, str] = {}

async def BenchmarkTest57109(request: Request, req: UserInput):
    json_value = req.payload
    request_state['last_input'] = json_value
    data = request_state['last_input']
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
