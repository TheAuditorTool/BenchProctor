# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
import base64
from starlette.responses import JSONResponse


async def BenchmarkTest75449(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    digest = str(data).encode().hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
