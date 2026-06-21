# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest70430(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    if cookie_value not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = cookie_value
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'X-Echo': str(processed)})
