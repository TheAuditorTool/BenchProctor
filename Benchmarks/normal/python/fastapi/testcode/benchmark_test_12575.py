# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
from app_runtime import db


async def BenchmarkTest12575(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    return HTMLResponse(Template(comment_value).render())
