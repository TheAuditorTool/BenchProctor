# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse


async def BenchmarkTest04703(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    digest = hashlib.sha1(str(multipart_value).encode()).hexdigest()
    return JSONResponse({'digest': str(digest)}, status_code=200)
