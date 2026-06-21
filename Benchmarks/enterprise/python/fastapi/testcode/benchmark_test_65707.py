# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
import os
import ast


async def BenchmarkTest65707(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    try:
        data = str(ast.literal_eval(cookie_value))
    except (ValueError, SyntaxError):
        data = cookie_value
    if os.environ.get("APP_ENV", "production") != "test":
        return HTMLResponse(Template(data).render())
    return {"updated": True}
