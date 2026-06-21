# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import json


async def BenchmarkTest50429(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = ' '.join(str(graphql_var).split())
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
