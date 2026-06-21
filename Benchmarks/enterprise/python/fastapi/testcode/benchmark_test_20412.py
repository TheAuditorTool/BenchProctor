# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse
from urllib.parse import urlparse
from starlette.responses import JSONResponse


async def BenchmarkTest20412(request: Request):
    origin_value = request.headers.get('origin', '')
    parsed = urlparse(origin_value)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    target_url = origin_value
    return RedirectResponse(url=str(target_url))
