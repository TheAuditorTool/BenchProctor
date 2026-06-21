# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from fastapi import Form
import time


request_state: dict[str, str] = {}

async def BenchmarkTest69855(request: Request, field: str = Form('')):
    field_value = field
    request_state['last_input'] = field_value
    data = request_state['last_input']
    if time.time() > 1000000000:
        os.system('echo ' + str(data))
    return {"updated": True}
