# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import re
from starlette.responses import JSONResponse
from app_runtime import db


def relay_value(value):
    return value

async def BenchmarkTest55078(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = relay_value(db_value)
    if not re.fullmatch('^[\\w\\s<>\\"\'/().;=]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    return HTMLResponse('<div>' + str(processed) + '</div>')
