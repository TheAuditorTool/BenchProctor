# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest26973(request: Request):
    upload_name = (await request.form()).get('upload', '')
    ciphertext = bytes(b ^ 0x42 for b in str(upload_name).encode())
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
