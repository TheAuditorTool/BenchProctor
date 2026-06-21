# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html
import json


request_state: dict[str, str] = {}

async def BenchmarkTest71837(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    request_state['last_input'] = graphql_var
    data = request_state['last_input']
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
