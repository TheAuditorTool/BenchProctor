# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest24071(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    divisor = int(str(db_value)) if str(db_value).isdigit() else 1
    if divisor == 0:
        return JSONResponse({'error': 'zero division'}, status_code=400)
    result = 100 / divisor
    return {"updated": True}
