# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest25416(request: Request):
    auth_header = request.headers.get('authorization', '')
    ciphertext = bytes(b ^ 0x42 for b in str(auth_header).encode())
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
