# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import re
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''
def ensure_str(value):
    return str(value)

async def BenchmarkTest63891(request: Request, req: UserInput):
    json_value = req.payload
    data = ensure_str(json_value)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(processed), max_age=86400)
    return resp
