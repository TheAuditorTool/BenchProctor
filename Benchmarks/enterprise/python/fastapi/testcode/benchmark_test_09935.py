# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import re


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest09935(request: Request):
    host_value = request.headers.get('host', '')
    data = default_blank(host_value)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    return JSONResponse({'error': str(processed), 'stack': repr(locals())}, status_code=500)
