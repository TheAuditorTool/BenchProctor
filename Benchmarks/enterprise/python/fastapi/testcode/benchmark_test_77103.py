# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest77103(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = (lambda v: v.strip())(cookie_value)
    if len(str(data)) >= 4:
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
