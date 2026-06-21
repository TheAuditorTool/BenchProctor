# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
import json
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest73940(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = json.loads(db_value).get('value', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'X-Echo': str(processed)})
