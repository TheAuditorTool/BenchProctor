# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest07788(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    def normalize(value):
        return value.strip()
    data = normalize(db_value)
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
