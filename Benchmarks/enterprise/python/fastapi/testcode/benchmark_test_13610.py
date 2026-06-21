# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import json
import os


async def BenchmarkTest13610(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data, _sep, _rest = str(graphql_var).partition('\x00')
    os.environ['APP_USER_PREFERENCE'] = str(data)
    return JSONResponse({'config_set': 'APP_USER_PREFERENCE'}, status_code=200)
