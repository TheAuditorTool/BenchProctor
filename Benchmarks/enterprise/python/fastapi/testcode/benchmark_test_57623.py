# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse


async def BenchmarkTest57623(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(forwarded_ip)
    data = collected
    digest = str(data).encode().hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
