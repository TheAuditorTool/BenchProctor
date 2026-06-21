# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest29196(request: Request):
    origin_value = request.headers.get('origin', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(origin_value)
    data = collected
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
