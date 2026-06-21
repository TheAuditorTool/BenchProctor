# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import re
from app_runtime import db


async def BenchmarkTest41805(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(db_value)
    data = collected
    if re.search('[a-zA-Z0-9_-]+', str(data)):
        return JSONResponse({'validated': str(data)}, status_code=200)
    return {"updated": True}
