# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse


async def BenchmarkTest29103(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = '%s' % (auth_header,)
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
