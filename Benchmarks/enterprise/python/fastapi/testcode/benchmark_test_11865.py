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

async def BenchmarkTest11865(request: Request):
    user_id = request.query_params.get('id', '')
    data = handle(user_id)
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
