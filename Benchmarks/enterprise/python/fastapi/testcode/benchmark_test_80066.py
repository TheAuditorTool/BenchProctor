# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
from jinja2 import Environment
import json


async def BenchmarkTest80066(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    return HTMLResponse(Environment(autoescape=True).from_string('{{ value }}').render(value=data))
