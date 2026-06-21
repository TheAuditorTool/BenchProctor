# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
import re
from starlette.responses import JSONResponse
import json


def ensure_str(value):
    return str(value)

async def BenchmarkTest41979(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = ensure_str(graphql_var)
    if not re.fullmatch('^[\\w\\s<>\\"\'/(){}.*]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    return HTMLResponse(Template(processed).render())
