# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest40869(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(forwarded_ip)
    data = collected
    def _primary():
        eval(str(data))
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return {"updated": True}
