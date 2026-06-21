# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import json
import time


def relay_value(value):
    return value

async def BenchmarkTest31696(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = relay_value(graphql_var)
    if time.time() > 1000000000:
        return HTMLResponse('<div>' + str(data) + '</div>')
    return {"updated": True}
