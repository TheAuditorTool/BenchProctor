# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import urlparse
from fastapi import Form
from starlette.responses import JSONResponse
import socket


def ensure_str(value):
    return str(value)

async def BenchmarkTest16797(request: Request, field: str = Form('')):
    field_value = field
    data = ensure_str(field_value)
    parsed = urlparse(data)
    if not (parsed.hostname or '').endswith(('.prod.internal', '.pycdn.io')):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    target_url = data
    s = socket.create_connection((str(target_url), 80))
    s.close()
    return {"updated": True}
