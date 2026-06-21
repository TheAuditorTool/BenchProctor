# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import base64
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest15879(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = base64.b64decode(db_value).decode('utf-8', 'ignore')
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    os.system('echo ' + str(processed))
    return {"updated": True}
