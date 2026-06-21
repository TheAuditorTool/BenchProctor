# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from pydantic import BaseModel
from starlette.responses import JSONResponse
import urllib.request


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest46722(request: Request, req: UserInput):
    json_value = req.payload
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', json_value):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = json_value
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(processed)).read()
    return {"updated": True}
