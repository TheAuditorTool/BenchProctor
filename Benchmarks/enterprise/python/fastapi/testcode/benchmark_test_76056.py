# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
from jinja2 import Environment


async def BenchmarkTest76056(request: Request):
    user_id = request.query_params.get('id', '')
    data = user_id if user_id else 'default'
    return HTMLResponse(Environment(autoescape=True).from_string('safe block: {{ value }}').render(value=data))
