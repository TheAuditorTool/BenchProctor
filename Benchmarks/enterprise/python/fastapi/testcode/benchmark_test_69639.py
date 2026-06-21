# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest69639(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value}'
    if str(data) in ('localhost', 'internal-gateway'):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
