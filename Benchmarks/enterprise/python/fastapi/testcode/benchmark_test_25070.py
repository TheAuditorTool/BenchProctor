# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import json


async def BenchmarkTest25070(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data, _sep, _rest = str(graphql_var).partition('\x00')
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
