# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest72828(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = handle(upload_name)
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Content-Language': str(data)})
