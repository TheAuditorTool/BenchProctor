# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import base64
from app_runtime import db


async def BenchmarkTest52430(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = base64.b64decode(db_value).decode('utf-8', 'ignore')
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
