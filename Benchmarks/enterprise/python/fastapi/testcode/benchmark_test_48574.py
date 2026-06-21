# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import time


request_state: dict[str, str] = {}

async def BenchmarkTest48574(request: Request):
    user_id = request.query_params.get('id', '')
    request_state['last_input'] = user_id
    data = request_state['last_input']
    if time.time() > 1000000000:
        os.system('echo ' + str(data))
    return {"updated": True}
