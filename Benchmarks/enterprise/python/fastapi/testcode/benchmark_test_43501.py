# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html
from app_runtime import db


async def BenchmarkTest43501(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data, _sep, _rest = str(db_value).partition('\x00')
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
