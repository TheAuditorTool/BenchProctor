# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import json


async def BenchmarkTest49319(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    prefix = ''
    data = prefix + str(graphql_var)
    return HTMLResponse('<div>' + str(data) + '</div>')
