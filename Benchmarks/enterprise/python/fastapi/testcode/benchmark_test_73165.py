# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time


async def BenchmarkTest73165(request: Request):
    user_id = request.query_params.get('id', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(user_id)
    data = collected
    if time.time() > 1000000000:
        eval(str(data))
    return {"updated": True}
