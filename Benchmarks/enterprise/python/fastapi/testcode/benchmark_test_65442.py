# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest65442(request: Request):
    ua_value = request.headers.get('user-agent', '')
    kind = 'json' if str(ua_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = ua_value
            data = parsed
        case _:
            data = ua_value
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(data),))
    return JSONResponse({'secret': str(secret)}, status_code=200)
