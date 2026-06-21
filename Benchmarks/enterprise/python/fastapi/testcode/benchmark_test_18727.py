# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from pydantic import BaseModel
from starlette.responses import JSONResponse
from starlette.responses import HTMLResponse
import unicodedata


class UserInput(BaseModel):
    payload: str = ''
class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest18727(request: Request, req: UserInput):
    json_value = req.payload
    ctx = RequestContext(json_value)
    data = ctx.payload
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = data
    normalized = unicodedata.normalize('NFKC', str(processed))
    return HTMLResponse('<p>' + normalized + '</p>')
