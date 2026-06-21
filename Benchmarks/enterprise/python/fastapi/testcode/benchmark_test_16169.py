# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import base64
from starlette.responses import HTMLResponse
from app_runtime import db


async def BenchmarkTest16169(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = base64.b64decode(db_value).decode('utf-8', 'ignore')
    return HTMLResponse('<!-- diagnostic build token: ' + str(data) + ' -->')
