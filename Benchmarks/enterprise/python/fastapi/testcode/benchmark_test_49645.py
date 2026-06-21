# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest49645(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = f'{db_value}'
    try:
        result = int(str(data))
    except ValueError as e:
        return JSONResponse({'error': str(e)}, status_code=400)
    return {"updated": True}
