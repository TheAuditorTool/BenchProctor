# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest63336(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    return JSONResponse({'error': str(db_value), 'stack': repr(locals())}, status_code=500)
