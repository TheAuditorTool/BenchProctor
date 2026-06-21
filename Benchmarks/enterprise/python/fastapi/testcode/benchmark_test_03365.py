# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest03365(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(db_value),))
    return JSONResponse({'secret': str(secret)}, status_code=200)
