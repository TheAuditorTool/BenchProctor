# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest46395(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    if forwarded_ip:
        data = forwarded_ip
    else:
        data = ''
    record = db.fetch_one('SELECT * FROM documents WHERE id = ?', (str(data),))
    return JSONResponse({'record': str(record)}, status_code=200)
