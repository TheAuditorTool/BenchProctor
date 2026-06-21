# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest16360(request: Request):
    host_value = request.headers.get('host', '')
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(host_value),))
    return JSONResponse({'secret': str(secret)}, status_code=200)
