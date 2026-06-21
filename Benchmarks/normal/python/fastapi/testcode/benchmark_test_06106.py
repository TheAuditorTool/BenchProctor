# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


def relay_value(value):
    return value

async def BenchmarkTest06106(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = relay_value(cookie_value)
    record = db.fetch_one('SELECT * FROM documents WHERE id = ?', (str(data),))
    return JSONResponse({'record': str(record)}, status_code=200)
