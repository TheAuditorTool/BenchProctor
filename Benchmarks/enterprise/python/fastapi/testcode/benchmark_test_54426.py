# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from urllib.parse import urlparse
from fastapi import Form
from starlette.responses import JSONResponse


async def BenchmarkTest54426(request: Request, field: str = Form('')):
    field_value = field
    parsed = urlparse(field_value)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    target_url = field_value
    requests.get(str(target_url))
    return {"updated": True}
