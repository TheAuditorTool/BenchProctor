# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse
from app_runtime import auth_check


request_state: dict[str, str] = {}

async def BenchmarkTest39136(request: Request):
    secret_value = ['s3cr3t_key_test_xyz'][0]
    request_state['last_input'] = secret_value
    data = request_state['last_input']
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    auth_check('user', processed)
    return {"updated": True}
