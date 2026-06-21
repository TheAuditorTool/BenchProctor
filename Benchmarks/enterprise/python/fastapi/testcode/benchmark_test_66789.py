# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest66789(request: Request, req: UserInput):
    json_value = req.payload
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(json_value), max_age=86400)
    return resp
