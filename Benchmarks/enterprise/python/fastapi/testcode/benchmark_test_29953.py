# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest29953(request: Request):
    origin_value = request.headers.get('origin', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(origin_value)
    data = collected
    int(str(data))
    return {"updated": True}
