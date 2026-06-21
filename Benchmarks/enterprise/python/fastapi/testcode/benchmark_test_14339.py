# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html
from app_runtime import db


async def BenchmarkTest14339(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    parts = str(db_value).split(',')
    data = ','.join(parts)
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
