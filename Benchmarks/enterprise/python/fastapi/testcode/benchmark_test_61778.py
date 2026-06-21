# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest61778(request: Request):
    ua_value = request.headers.get('user-agent', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(ua_value)
    data = collected
    os.remove(str(data))
    return {"updated": True}
