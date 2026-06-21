# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse
from types import SimpleNamespace


async def BenchmarkTest36262(request: Request):
    referer_value = request.headers.get('referer', '')
    ns = SimpleNamespace(payload=referer_value)
    data = getattr(ns, 'payload')
    def _primary():
        return RedirectResponse(url=str(data))
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
