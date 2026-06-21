# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
from jinja2 import Environment
from app_runtime import db


async def BenchmarkTest04980(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = f'{comment_value}'
    return HTMLResponse(Environment(autoescape=True).from_string('{{ value }}').render(value=data))
