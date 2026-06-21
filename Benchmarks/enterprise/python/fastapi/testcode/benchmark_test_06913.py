# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest06913(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    try:
        int(str(db_value))
    except ValueError:
        return JSONResponse({'error': 'invalid'}, status_code=400)
    return {"updated": True}
