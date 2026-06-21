# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse
import tempfile


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest07617(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = handle(xml_value)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(processed))
    return {"updated": True}
