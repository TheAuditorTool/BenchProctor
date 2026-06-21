# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
import json
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest10193(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = json.loads(db_value).get('value', '')
    random.seed(int(data) if str(data).isdigit() else 99)
    token = random.randint(0, 99)
    return JSONResponse({'token': str(token)}, status_code=200)
