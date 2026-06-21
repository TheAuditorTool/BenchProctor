# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os


request_state: dict[str, str] = {}

async def BenchmarkTest03687(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    request_state['last_input'] = env_value
    data = request_state['last_input']
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Access-Control-Allow-Origin': str(data)})
