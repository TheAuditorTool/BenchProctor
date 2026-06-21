# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
import json


async def BenchmarkTest75498(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    def normalize(value):
        return value.strip()
    data = normalize(graphql_var)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    return HTMLResponse(Template(processed).render())
