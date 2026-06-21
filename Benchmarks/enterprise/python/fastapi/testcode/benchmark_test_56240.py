# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
from app_runtime import db


async def BenchmarkTest56240(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    prefix = ''
    data = prefix + str(db_value)
    return HTMLResponse('<html><body><h1>' + str(data) + '</h1></body></html>')
