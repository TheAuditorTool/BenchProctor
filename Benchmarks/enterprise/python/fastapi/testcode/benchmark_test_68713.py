# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest68713(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    prefix = ''
    data = prefix + str(multipart_value)
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
