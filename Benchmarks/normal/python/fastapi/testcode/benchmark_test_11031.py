# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
from starlette.responses import JSONResponse
from app_runtime import db


def ensure_str(value):
    return str(value)

async def BenchmarkTest11031(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = ensure_str(db_value)
    random.seed(int(data) if str(data).isdigit() else 1337)
    token = random.randint(0, 100000)
    return JSONResponse({'token': str(token)}, status_code=200)
