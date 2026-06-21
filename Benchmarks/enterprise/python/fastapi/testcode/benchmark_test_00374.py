# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse


def to_text(value):
    return str(value).strip()

async def BenchmarkTest00374(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = to_text(env_value)
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
