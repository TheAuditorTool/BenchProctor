# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import requests


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest51814(request: Request):
    path_value = request.path_params.get('id', '')
    data = handle(path_value)
    if str(data).lower() not in ('true', 'false'):
        return JSONResponse({'error': 'invalid boolean'}, status_code=400)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return {"updated": True}
