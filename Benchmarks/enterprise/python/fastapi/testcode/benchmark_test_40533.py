# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import json
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest40533(request: Request, req: UserInput):
    json_value = req.payload
    data = json.loads(json_value).get('value', '')
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
