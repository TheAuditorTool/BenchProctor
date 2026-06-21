# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest63748(request: Request):
    origin_value = request.headers.get('origin', '')
    ciphertext = bytes(b ^ 0x42 for b in str(origin_value).encode())
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
