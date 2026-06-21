# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
from app_runtime import db


async def BenchmarkTest33544(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    return HTMLResponse(Template(db_value).render())
