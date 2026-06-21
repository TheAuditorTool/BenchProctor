# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse


def relay_value(value):
    return value

async def BenchmarkTest80452(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = relay_value(forwarded_ip)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Content-Language': str(processed)})
