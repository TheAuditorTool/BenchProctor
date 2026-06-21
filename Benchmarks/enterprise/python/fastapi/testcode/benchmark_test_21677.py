# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from starlette.responses import HTMLResponse


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest21677(request: Request):
    user_id = request.query_params.get('id', '')
    data = handle(user_id)
    return HTMLResponse('<!-- diagnostic build token: ' + str(data) + ' -->')
