# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time


async def BenchmarkTest51596(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(raw_body)
    data = collected
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
