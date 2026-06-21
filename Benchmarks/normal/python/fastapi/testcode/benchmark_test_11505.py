# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse
from urllib.parse import urlparse
from starlette.responses import JSONResponse


async def BenchmarkTest11505(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    parsed = urlparse(forwarded_ip)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    target_url = forwarded_ip
    return RedirectResponse(url=str(target_url))
