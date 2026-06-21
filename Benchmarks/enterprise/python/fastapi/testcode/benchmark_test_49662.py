# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest49662(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    record = db.fetch_one('SELECT * FROM documents WHERE id = ?', (str(data),))
    return JSONResponse({'record': str(record)}, status_code=200)
