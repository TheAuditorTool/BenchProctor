# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest42692(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    if len(str(cookie_value)) >= 4:
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
