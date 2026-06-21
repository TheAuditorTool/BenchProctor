# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import re
from fastapi import Form


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest72275(request: Request, field: str = Form('')):
    field_value = field
    data = handle(field_value)
    processed = re.sub(r'\d+', '****', str(data))
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(processed), max_age=86400)
    return resp
