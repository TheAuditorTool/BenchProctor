# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os
from app_runtime import db


async def BenchmarkTest61444(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = db_value if db_value else 'default'
    entries = os.listdir(str(data))
    return JSONResponse({'listing': entries}, status_code=200)
