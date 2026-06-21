# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
from app_runtime import db


async def BenchmarkTest30628(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    if db_value:
        data = db_value
    else:
        data = ''
    return HTMLResponse('<html><body><h1>' + str(data) + '</h1></body></html>')
