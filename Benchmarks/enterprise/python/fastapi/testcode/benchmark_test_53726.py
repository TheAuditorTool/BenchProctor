# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def to_text(value):
    return str(value).strip()

async def BenchmarkTest53726(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = to_text(auth_header)
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
