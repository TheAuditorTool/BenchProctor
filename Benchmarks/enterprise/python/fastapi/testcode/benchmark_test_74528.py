# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from starlette.responses import HTMLResponse
import json


def to_text(value):
    return str(value).strip()

async def BenchmarkTest74528(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = to_text(graphql_var)
    return HTMLResponse('<!-- diagnostic build token: ' + str(data) + ' -->')
