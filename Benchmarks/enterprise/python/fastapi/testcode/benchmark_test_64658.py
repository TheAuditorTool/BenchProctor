# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from urllib.parse import urlparse
from starlette.responses import JSONResponse
from starlette.responses import HTMLResponse


async def BenchmarkTest64658(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    parsed = urlparse(xml_value)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    target_url = xml_value
    return HTMLResponse('<script src="' + str(target_url) + '"></script>')
