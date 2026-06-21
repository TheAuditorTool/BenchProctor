# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
from jinja2 import Environment
from urllib.parse import unquote


async def BenchmarkTest37923(request: Request):
    user_id = request.query_params.get('id', '')
    data = unquote(user_id)
    return HTMLResponse(Environment(autoescape=True).from_string('{{ value }}').render(value=data))
