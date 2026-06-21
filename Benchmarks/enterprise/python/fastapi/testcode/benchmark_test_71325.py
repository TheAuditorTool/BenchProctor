# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import re
import requests
from starlette.responses import JSONResponse


request_state: dict[str, str] = {}

async def BenchmarkTest71325(request: Request):
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    request_state['last_input'] = api_value
    data = request_state['last_input']
    if not re.fullmatch('^[\\w\\s./\\\\:_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    with open('/var/uploads/' + str(processed), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
