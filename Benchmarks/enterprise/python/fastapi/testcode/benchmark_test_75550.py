# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest75550(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    arr = [10, 20, 30, 40, 50]
    idx = int(str(db_value))
    return JSONResponse({'lookup': arr[idx]}, status_code=200)
