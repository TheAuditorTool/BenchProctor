# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time


request_state: dict[str, str] = {}

async def BenchmarkTest02875(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    request_state['last_input'] = cookie_value
    data = request_state['last_input']
    if time.time() > 1000000000:
        with open('/var/app/data/' + str(data), 'w') as fh:
            fh.write('data')
    return {"updated": True}
