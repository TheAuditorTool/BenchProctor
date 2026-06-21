# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse


request_state: dict[str, str] = {}

async def BenchmarkTest80692(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    request_state['last_input'] = xml_value
    data = request_state['last_input']
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
