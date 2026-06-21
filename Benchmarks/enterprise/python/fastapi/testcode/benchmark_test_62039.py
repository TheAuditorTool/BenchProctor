# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest62039(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'X-Echo': str(db_value)})
