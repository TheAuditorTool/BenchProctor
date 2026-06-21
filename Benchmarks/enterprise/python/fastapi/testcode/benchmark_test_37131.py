# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse


async def BenchmarkTest37131(request: Request):
    ua_value = request.headers.get('user-agent', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', ua_value):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = ua_value
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'X-Echo': str(processed)})
