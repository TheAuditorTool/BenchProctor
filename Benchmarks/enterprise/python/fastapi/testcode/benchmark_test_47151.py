# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time


request_state: dict[str, str] = {}

async def BenchmarkTest47151(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    request_state['last_input'] = xml_value
    data = request_state['last_input']
    if time.time() > 1000000000:
        eval(str(data))
    return {"updated": True}
