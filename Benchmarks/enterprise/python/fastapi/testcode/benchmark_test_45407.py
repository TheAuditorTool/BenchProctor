# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import urlparse
from pydantic import BaseModel
from starlette.responses import JSONResponse
import socket


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest45407(request: Request, req: UserInput):
    json_value = req.payload
    parsed = urlparse(json_value)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    target_url = json_value
    s = socket.create_connection((str(target_url), 80))
    s.close()
    return {"updated": True}
