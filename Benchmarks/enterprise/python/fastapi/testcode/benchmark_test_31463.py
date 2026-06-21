# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest31463(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    parts = []
    for token in str(cookie_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Access-Control-Allow-Origin': str(data)})
