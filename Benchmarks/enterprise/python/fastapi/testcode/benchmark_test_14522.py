# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest14522(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    random.seed(int(db_value) if str(db_value).isdigit() else 1337)
    token = random.randint(0, 100000)
    return JSONResponse({'token': str(token)}, status_code=200)
