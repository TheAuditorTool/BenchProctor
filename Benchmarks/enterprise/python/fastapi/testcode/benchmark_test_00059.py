# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest00059(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    try:
        result = int(str(db_value))
    except ValueError as e:
        return JSONResponse({'error': str(e)}, status_code=400)
    return {"updated": True}
