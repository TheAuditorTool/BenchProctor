# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest63831(request: Request):
    origin_value = request.headers.get('origin', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(origin_value)
    data = collected
    def _primary():
        eval(str(data))
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return {"updated": True}
