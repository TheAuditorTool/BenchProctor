# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import base64
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest66803(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(data),))
    return JSONResponse({'secret': str(secret)}, status_code=200)
