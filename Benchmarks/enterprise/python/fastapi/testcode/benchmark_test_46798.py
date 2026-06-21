# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse
import re
from starlette.responses import JSONResponse


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest46798(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = handle(raw_body)
    if not re.fullmatch('^[\\w\\s./\\\\:_?&=\\-@]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    return RedirectResponse(url=str(processed))
