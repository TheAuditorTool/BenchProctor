# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse


def relay_value(value):
    return value

async def BenchmarkTest15934(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = relay_value(multipart_value)
    digest = str(data).encode().hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
