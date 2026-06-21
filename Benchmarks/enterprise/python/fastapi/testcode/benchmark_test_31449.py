# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from starlette.responses import HTMLResponse
import json
from app_runtime import db


async def BenchmarkTest31449(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    try:
        data = json.loads(db_value).get('value', db_value)
    except (json.JSONDecodeError, AttributeError):
        data = db_value
    return HTMLResponse('<!-- diagnostic build token: ' + str(data) + ' -->')
