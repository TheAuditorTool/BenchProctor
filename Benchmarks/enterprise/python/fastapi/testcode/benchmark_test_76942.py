# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import re


def relay_value(value):
    return value

async def BenchmarkTest76942(request: Request):
    referer_value = request.headers.get('referer', '')
    data = relay_value(referer_value)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    return JSONResponse({'error': str(processed), 'stack': repr(locals())}, status_code=500)
