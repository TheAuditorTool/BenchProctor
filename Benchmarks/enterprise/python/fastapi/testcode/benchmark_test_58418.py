# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import re
from starlette.responses import JSONResponse


request_state: dict[str, str] = {}

async def BenchmarkTest58418(request: Request):
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    request_state['last_input'] = secret_value
    data = request_state['last_input']
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    requests.get('https://api.pycdn.io/v1/data', headers={'Authorization': 'Bearer ' + str(processed)})
    return {"updated": True}
