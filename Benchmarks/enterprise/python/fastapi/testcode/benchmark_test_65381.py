# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import json


async def BenchmarkTest65381(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(graphql_var), secure=True, httponly=True, samesite='Strict')
    return resp
