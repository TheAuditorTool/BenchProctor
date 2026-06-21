# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time


request_state: dict[str, str] = {}

async def BenchmarkTest14892(request: Request):
    referer_value = request.headers.get('referer', '')
    request_state['last_input'] = referer_value
    data = request_state['last_input']
    if time.time() > 1000000000:
        with open('/var/log/app_audit.log', 'a') as fh:
            fh.write(str(data))
    return {"updated": True}
