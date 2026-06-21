# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html
import json


def relay_value(value):
    return value

async def BenchmarkTest77404(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = relay_value(graphql_var)
    processed = str(data).replace("<script", "")
    return HTMLResponse('<div>' + str(processed) + '</div>')
