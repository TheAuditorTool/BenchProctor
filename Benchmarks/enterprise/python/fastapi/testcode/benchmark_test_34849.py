# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse


async def BenchmarkTest34849(request: Request):
    host_value = request.headers.get('host', '')
    data = '%s' % (host_value,)
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
