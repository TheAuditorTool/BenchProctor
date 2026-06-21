# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os
from app_runtime import db


request_state: dict[str, str] = {}

async def BenchmarkTest44967(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    request_state['last_input'] = comment_value
    data = request_state['last_input']
    entries = os.listdir(str(data))
    return JSONResponse({'listing': entries}, status_code=200)
