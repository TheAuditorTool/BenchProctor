# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import bleach
import json


async def BenchmarkTest23427(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = str(graphql_var).replace('\x00', '')
    processed = bleach.clean(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
