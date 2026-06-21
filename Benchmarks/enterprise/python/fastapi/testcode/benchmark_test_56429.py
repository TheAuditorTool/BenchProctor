# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
from app_runtime import db


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest56429(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = default_blank(db_value)
    processed = data[:64]
    return HTMLResponse('<div>' + str(processed) + '</div>')
