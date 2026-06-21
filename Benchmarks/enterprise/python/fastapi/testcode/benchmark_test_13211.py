# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import time


request_state: dict[str, str] = {}

async def BenchmarkTest13211(request: Request):
    ua_value = request.headers.get('user-agent', '')
    request_state['last_input'] = ua_value
    data = request_state['last_input']
    if time.time() > 1000000000:
        os.unlink('/var/app/data/' + str(data))
    return {"updated": True}
