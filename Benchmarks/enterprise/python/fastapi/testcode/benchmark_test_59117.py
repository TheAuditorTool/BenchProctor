# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest59117(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    result = db.fetch_one('SELECT name FROM users WHERE id = ?', (str(forwarded_ip),))
    value = result['name']
    return JSONResponse({'name': str(value)}, status_code=200)
