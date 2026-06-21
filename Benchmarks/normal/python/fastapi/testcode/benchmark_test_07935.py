# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
import json


async def BenchmarkTest07935(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    parts = str(graphql_var).split(',')
    data = ','.join(parts)
    return HTMLResponse(Template(data).render())
