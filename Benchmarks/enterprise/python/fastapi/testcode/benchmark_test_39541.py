# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse


async def BenchmarkTest39541(request: Request):
    auth_header = request.headers.get('authorization', '')
    pending = list(str(auth_header).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    digest = hashlib.sha256(('static_salt_123' + str(data)).encode()).hexdigest()
    return JSONResponse({'digest': str(digest)}, status_code=200)
