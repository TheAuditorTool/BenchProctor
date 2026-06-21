# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest32943(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = json.loads(db_value).get('value', '')
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return JSONResponse({'lookup': arr[idx]}, status_code=200)
