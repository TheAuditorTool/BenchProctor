# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from urllib.parse import urlparse
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest17785(request: Request, req: UserInput):
    json_value = req.payload
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(json_value)
    data = collected
    parsed = urlparse(data)
    if not (parsed.hostname or '').endswith(('.prod.internal', '.pycdn.io')):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    target_url = data
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Access-Control-Allow-Origin': str(target_url)})
