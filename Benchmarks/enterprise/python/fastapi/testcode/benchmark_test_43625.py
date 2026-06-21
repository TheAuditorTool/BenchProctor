# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest43625(request: Request):
    referer_value = request.headers.get('referer', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(referer_value)
    data = collected
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
