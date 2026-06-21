# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest14605(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value}'
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Content-Language': str(data)})
