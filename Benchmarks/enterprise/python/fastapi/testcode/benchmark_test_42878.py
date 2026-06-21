# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
import re
from starlette.responses import JSONResponse


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest42878(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = handle(xml_value)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    digest = hashlib.md5(str(processed).encode()).hexdigest()
    return JSONResponse({'digest': str(digest)}, status_code=200)
