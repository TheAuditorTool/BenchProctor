# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import socket


async def BenchmarkTest36957(request: Request):
    referer_value = request.headers.get('referer', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(referer_value)
    data = collected
    def _primary():
        s = socket.create_connection((str(data), 80))
        s.close()
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return {"updated": True}
