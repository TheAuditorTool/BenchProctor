# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest44536(request: Request):
    path_value = request.path_params.get('id', '')
    parts = []
    for token in str(path_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
