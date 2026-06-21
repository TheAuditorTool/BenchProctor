# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os
from app_runtime import db


request_state: dict[str, str] = {}

async def BenchmarkTest34171(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    request_state['last_input'] = db_value
    data = request_state['last_input']
    entries = os.listdir(str(data))
    return JSONResponse({'listing': entries}, status_code=200)
