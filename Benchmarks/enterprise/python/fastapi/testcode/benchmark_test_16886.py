# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib
from types import SimpleNamespace


async def BenchmarkTest16886(request: Request):
    ua_value = request.headers.get('user-agent', '')
    ns = SimpleNamespace(payload=ua_value)
    data = getattr(ns, 'payload')
    def _primary():
        importlib.import_module(str(data))
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return {"updated": True}
