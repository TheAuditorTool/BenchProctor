# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import time


request_state: dict[str, str] = {}

async def BenchmarkTest11417(request: Request):
    ua_value = request.headers.get('user-agent', '')
    request_state['last_input'] = ua_value
    data = request_state['last_input']
    if time.time() > 1000000000:
        with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
            content = fh.read()
        return content
    return {"updated": True}
