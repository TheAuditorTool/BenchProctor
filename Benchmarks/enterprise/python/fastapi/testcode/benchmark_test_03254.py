# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from types import SimpleNamespace


async def BenchmarkTest03254(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    ns = SimpleNamespace(payload=cookie_value)
    data = getattr(ns, 'payload')
    def _primary():
        eval(str(data))
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return {"updated": True}
