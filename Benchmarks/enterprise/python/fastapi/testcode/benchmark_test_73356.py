# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse


async def BenchmarkTest73356(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(forwarded_ip)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = forwarded_ip
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Content-Language': str(processed)})
