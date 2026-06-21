# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
import base64
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest48350(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = base64.b64decode(db_value).decode('utf-8', 'ignore')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    eval(str(processed))
    return {"updated": True}
