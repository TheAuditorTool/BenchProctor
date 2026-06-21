# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
from app_runtime import db


async def BenchmarkTest17019(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    return HTMLResponse('<div>' + str(db_value) + '</div>')
