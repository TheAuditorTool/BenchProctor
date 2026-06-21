# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import urlparse
from dataclasses import dataclass
from starlette.responses import JSONResponse
import socket


@dataclass
class FormData:
    payload: str

async def BenchmarkTest31265(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = FormData(payload=raw_body).payload
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    target_url = data
    s = socket.create_connection((str(target_url), 80))
    s.close()
    return {"updated": True}
