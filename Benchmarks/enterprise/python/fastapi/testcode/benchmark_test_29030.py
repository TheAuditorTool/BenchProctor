# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time


async def BenchmarkTest29030(request: Request):
    ua_value = request.headers.get('user-agent', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(ua_value)
    data = collected
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
