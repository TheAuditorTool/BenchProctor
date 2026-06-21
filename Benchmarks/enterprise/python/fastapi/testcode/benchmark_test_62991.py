# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import html
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest62991(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(db_value)
    data = collected
    processed = str(data).replace("<script", "")
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Content-Language': str(processed)})
