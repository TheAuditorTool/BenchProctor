# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest04854(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(db_value)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = db_value
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'X-Echo': str(processed)})
