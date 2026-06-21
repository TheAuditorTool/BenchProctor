# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
from app_runtime import db


async def BenchmarkTest01767(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = ' '.join(str(comment_value).split())
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    return HTMLResponse(Template(processed).render())
