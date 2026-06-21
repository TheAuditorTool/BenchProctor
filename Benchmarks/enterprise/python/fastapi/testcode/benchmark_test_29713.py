# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse
import json


request_state: dict[str, str] = {}

async def BenchmarkTest29713(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    request_state['last_input'] = graphql_var
    data = request_state['last_input']
    processed = data[:64]
    return RedirectResponse(url=str(processed))
