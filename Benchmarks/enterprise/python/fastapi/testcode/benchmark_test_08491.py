# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html
import json


async def BenchmarkTest08491(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = (lambda v: v.strip())(graphql_var)
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
