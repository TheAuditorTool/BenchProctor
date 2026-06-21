# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
import json
from pydantic import BaseModel
from starlette.responses import JSONResponse
import urllib.request


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest00286(request: Request, req: UserInput):
    json_value = req.payload
    data = json.loads(json_value).get('value', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(processed)).read()
    return {"updated": True}
