# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os


request_state: dict[str, str] = {}

async def BenchmarkTest46035(request: Request):
    host_value = request.headers.get('host', '')
    request_state['last_input'] = host_value
    data = request_state['last_input']
    entries = os.listdir(str(data))
    return JSONResponse({'listing': entries}, status_code=200)
