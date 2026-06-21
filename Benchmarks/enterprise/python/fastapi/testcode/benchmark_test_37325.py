# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from pydantic import BaseModel
from types import SimpleNamespace


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest37325(request: Request, req: UserInput):
    json_value = req.payload
    ns = SimpleNamespace(payload=json_value)
    data = getattr(ns, 'payload')
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
