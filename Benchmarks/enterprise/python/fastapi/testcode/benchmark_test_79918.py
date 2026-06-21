# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse


def relay_value(value):
    return value

async def BenchmarkTest79918(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = relay_value(auth_header)
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    return JSONResponse({'digest': str(digest)}, status_code=200)
