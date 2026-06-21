# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from types import SimpleNamespace


async def BenchmarkTest73508(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    ns = SimpleNamespace(payload=header_value)
    data = getattr(ns, 'payload')
    def _primary():
        exec(str(data))
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return {"updated": True}
