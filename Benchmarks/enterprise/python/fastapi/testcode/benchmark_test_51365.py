# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from urllib.parse import urlparse
from starlette.responses import JSONResponse
from starlette.responses import HTMLResponse


async def BenchmarkTest51365(request: Request):
    upload_name = (await request.form()).get('upload', '')
    parsed = urlparse(upload_name)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    target_url = upload_name
    return HTMLResponse('<script src="' + str(target_url) + '"></script>')
