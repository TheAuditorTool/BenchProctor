# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import json
import unicodedata


request_state: dict[str, str] = {}

async def BenchmarkTest43970(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    request_state['last_input'] = graphql_var
    data = request_state['last_input']
    normalized = unicodedata.normalize('NFKC', str(data))
    return HTMLResponse('<p>' + normalized + '</p>')
