# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest24384(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value}'
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'X-Echo': str(data)})
