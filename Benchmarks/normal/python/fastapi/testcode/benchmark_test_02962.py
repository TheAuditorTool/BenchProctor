# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse


async def BenchmarkTest02962(request: Request):
    origin_value = request.headers.get('origin', '')
    data = '%s' % str(origin_value)
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
