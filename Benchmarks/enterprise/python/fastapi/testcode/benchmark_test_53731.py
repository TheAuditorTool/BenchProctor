# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest53731(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    trusted_claim = str(db_value)
    return JSONResponse({'trusted': trusted_claim}, status_code=200)
