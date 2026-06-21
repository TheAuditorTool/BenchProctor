# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
from app_runtime import db


request_state: dict[str, str] = {}

async def BenchmarkTest02752(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    request_state['last_input'] = comment_value
    data = request_state['last_input']
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    return HTMLResponse(Template(processed).render())
