# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


def relay_value(value):
    return value

async def BenchmarkTest62062(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = relay_value(ua_value)
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(data),))
    return JSONResponse({'secret': str(secret)}, status_code=200)
