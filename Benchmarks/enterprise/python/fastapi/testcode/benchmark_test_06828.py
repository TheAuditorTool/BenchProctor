# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
import json
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest06828(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = json.loads(db_value).get('value', '')
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
