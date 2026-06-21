# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest80403(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = '{}'.format(cookie_value)
    divisor = int(str(data)) if str(data).isdigit() else 1
    if divisor == 0:
        return JSONResponse({'error': 'zero division'}, status_code=400)
    result = 100 / divisor
    return {"updated": True}
