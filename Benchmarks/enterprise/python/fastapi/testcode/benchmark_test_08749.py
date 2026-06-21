# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html
from app_runtime import db


request_state: dict[str, str] = {}

async def BenchmarkTest08749(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    request_state['last_input'] = db_value
    data = request_state['last_input']
    processed = html.escape(data)
    return HTMLResponse('<img src="' + str(processed) + '">')
