# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse


async def BenchmarkTest47643(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    if multipart_value:
        data = multipart_value
    else:
        data = ''
    digest = str(data).encode().hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
