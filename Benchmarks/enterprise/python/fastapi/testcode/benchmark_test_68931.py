# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from pydantic import BaseModel
from starlette.responses import JSONResponse
from starlette.responses import RedirectResponse
import urllib.parse


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest68931(request: Request, req: UserInput):
    json_value = req.payload
    data = f'{json_value}'
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(processed))
    return RedirectResponse(url=target)
