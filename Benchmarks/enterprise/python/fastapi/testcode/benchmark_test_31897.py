# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest31897(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(cookie_value),))
    return JSONResponse({'secret': str(secret)}, status_code=200)
