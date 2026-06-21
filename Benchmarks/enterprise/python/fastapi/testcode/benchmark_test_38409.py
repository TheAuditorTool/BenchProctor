# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest38409(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(db_value)
    data = collected
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return JSONResponse({'token': str(token)}, status_code=200)
