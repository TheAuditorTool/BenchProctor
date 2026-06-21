# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest22688(request: Request, req: UserInput):
    json_value = req.payload
    data = json_value if json_value else 'default'
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
