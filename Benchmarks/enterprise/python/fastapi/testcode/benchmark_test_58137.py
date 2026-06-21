# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import json


async def BenchmarkTest58137(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = str(graphql_var).replace('\x00', '')
    return HTMLResponse('<html><body><h1>' + str(data) + '</h1></body></html>')
