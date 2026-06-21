# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import time


request_state: dict[str, str] = {}

async def BenchmarkTest21180(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    request_state['last_input'] = env_value
    data = request_state['last_input']
    if time.time() > 1000000000:
        with open('/var/uploads/' + str(data), 'wb') as fh:
            fh.write(b'data')
    return {"updated": True}
