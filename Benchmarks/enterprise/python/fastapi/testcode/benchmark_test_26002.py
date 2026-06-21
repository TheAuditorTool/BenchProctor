# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time


request_state: dict[str, str] = {}

async def BenchmarkTest26002(request: Request):
    path_value = request.path_params.get('id', '')
    request_state['last_input'] = path_value
    data = request_state['last_input']
    if time.time() > 1000000000:
        eval(str(data))
    return {"updated": True}
