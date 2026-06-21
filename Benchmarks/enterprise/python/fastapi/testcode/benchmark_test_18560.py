# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
from starlette.responses import JSONResponse
from starlette.responses import RedirectResponse
import urllib.parse


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest18560(request: Request, req: UserInput):
    json_value = req.payload
    data = ' '.join(str(json_value).split())
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(processed))
    return RedirectResponse(url=target)
