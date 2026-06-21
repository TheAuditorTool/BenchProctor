# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest74205(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = handle(upload_name)
    return HTMLResponse(str(data))
