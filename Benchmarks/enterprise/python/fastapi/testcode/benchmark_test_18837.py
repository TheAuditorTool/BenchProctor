# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest18837(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    try:
        result = int(str(cookie_value))
    except ValueError as e:
        return JSONResponse({'error': str(e)}, status_code=400)
    return {"updated": True}
