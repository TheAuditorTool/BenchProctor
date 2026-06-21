# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from urllib.parse import urlparse
from pydantic import BaseModel
from starlette.responses import JSONResponse


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest55947(request: Request, req: UserInput):
    json_value = req.payload
    parsed = urlparse(json_value)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    target_url = json_value
    _resp = requests.get(str(target_url))
    exec(_resp.text)
    return {"updated": True}
