# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html
import json
from types import SimpleNamespace


async def BenchmarkTest70413(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    ns = SimpleNamespace(payload=graphql_var)
    data = getattr(ns, 'payload')
    processed = str(data).replace("<script", "")
    return HTMLResponse('<img src="' + str(processed) + '">')
