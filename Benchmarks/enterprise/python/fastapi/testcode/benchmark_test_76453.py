# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html
import base64
from app_runtime import db


async def BenchmarkTest76453(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = base64.b64decode(db_value).decode('utf-8', 'ignore')
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
