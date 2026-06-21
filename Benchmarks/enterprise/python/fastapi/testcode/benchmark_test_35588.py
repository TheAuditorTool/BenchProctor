# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse


def to_text(value):
    return str(value).strip()

async def BenchmarkTest35588(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = to_text(ua_value)
    digest = hashlib.sha1(str(data).encode()).hexdigest()
    return JSONResponse({'digest': str(digest)}, status_code=200)
