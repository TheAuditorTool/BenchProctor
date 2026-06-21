# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from urllib.parse import urlparse
from urllib.parse import unquote
from fastapi import Form
from starlette.responses import JSONResponse
from starlette.responses import HTMLResponse


async def BenchmarkTest70840(request: Request, field: str = Form('')):
    field_value = field
    data = unquote(field_value)
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    target_url = data
    return HTMLResponse('<script src="' + str(target_url) + '"></script>')
