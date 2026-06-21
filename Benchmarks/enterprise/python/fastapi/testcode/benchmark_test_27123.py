# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html
import json


def ensure_str(value):
    return str(value)

async def BenchmarkTest27123(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = ensure_str(graphql_var)
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
