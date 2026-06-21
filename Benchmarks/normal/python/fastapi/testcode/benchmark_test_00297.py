# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
import base64
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest00297(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = base64.b64decode(db_value).decode('utf-8', 'ignore')
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return JSONResponse({'token': str(token)}, status_code=200)
