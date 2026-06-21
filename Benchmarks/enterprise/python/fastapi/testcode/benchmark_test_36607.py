# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest36607(request: Request):
    host_value = request.headers.get('host', '')
    result = db.fetch_one('SELECT name FROM users WHERE id = ?', (str(host_value),))
    value = result['name']
    return JSONResponse({'name': str(value)}, status_code=200)
