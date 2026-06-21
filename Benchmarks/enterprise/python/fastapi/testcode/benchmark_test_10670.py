# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest10670(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    prefix = ''
    data = prefix + str(forwarded_ip)
    result = db.fetch_one('SELECT name FROM users WHERE id = ?', (str(data),))
    value = result['name']
    return JSONResponse({'name': str(value)}, status_code=200)
