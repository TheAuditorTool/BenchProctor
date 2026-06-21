# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest44868(request: Request):
    origin_value = request.headers.get('origin', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(origin_value)
    data = collected
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
