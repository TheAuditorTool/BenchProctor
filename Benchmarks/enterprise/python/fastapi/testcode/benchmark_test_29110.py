# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse


async def BenchmarkTest29110(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = raw_body.decode('utf-8', 'ignore') if isinstance(raw_body, bytes) else raw_body
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
