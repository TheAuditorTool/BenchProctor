# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse
import json


async def BenchmarkTest41915(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = (lambda v: v.strip())(graphql_var)
    return RedirectResponse(url=str(data))
