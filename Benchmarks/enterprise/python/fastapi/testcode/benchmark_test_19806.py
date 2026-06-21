# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest19806(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    result = db.fetch_one('SELECT name FROM users WHERE id = ?', (str(header_value),))
    value = result['name']
    return JSONResponse({'name': str(value)}, status_code=200)
