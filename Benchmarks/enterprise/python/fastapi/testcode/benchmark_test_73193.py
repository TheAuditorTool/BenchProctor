# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
from app_runtime import db


async def BenchmarkTest73193(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    def normalize(value):
        return value.strip()
    data = normalize(db_value)
    return HTMLResponse('<div>' + str(data) + '</div>')
