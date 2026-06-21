# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest16289(request: Request):
    referer_value = request.headers.get('referer', '')
    data = default_blank(referer_value)
    digest = str(data).encode().hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
