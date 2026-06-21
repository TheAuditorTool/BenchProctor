# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time


request_state: dict[str, str] = {}

async def BenchmarkTest51108(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    request_state['last_input'] = header_value
    data = request_state['last_input']
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
