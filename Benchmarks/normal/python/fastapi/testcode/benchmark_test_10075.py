# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
from app_runtime import db


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest10075(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = coalesce_blank(comment_value)
    processed = data[:64]
    return HTMLResponse(Template(processed).render())
