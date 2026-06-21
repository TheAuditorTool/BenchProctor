# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
from jinja2 import Environment
from app_runtime import db


async def BenchmarkTest04550(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = f'{db_value}'
    return HTMLResponse(Environment(autoescape=True).from_string('safe block: {{ value }}').render(value=data))
