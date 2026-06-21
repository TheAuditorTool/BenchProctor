# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest33189(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = (lambda v: v.strip())(db_value)
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
