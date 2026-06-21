# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from starlette.responses import RedirectResponse
import urllib.parse


async def BenchmarkTest13243(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = json.loads(graphql_var).get('value', '')
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return RedirectResponse(url=target)
