# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import base64
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest33001(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = base64.b64decode(db_value).decode('utf-8', 'ignore')
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Content-Language': str(processed)})
