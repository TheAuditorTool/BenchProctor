# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest48448(request: Request):
    ua_value = request.headers.get('user-agent', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(ua_value)
    data = collected
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
