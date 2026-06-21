# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import json


async def BenchmarkTest31361(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    parts = str(graphql_var).split(',')
    data = ','.join(parts)
    return HTMLResponse(str(data))
