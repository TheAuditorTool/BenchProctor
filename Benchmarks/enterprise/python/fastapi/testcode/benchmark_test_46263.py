# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse


request_state: dict[str, str] = {}

async def BenchmarkTest46263(request: Request):
    auth_header = request.headers.get('authorization', '')
    request_state['last_input'] = auth_header
    data = request_state['last_input']
    allowed = {'config.json', 'index.html', 'readme.md'}
    if data not in allowed:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    checked_path = '/var/app/data/' + data
    with open(checked_path, 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
