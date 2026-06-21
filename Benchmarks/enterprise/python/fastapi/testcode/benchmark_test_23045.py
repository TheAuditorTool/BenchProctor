# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import base64
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest23045(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = base64.b64decode(db_value).decode('utf-8', 'ignore')
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'X-Echo': str(data)})
