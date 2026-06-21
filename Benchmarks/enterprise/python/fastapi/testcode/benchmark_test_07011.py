# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from types import SimpleNamespace


async def BenchmarkTest07011(request: Request):
    user_id = request.query_params.get('id', '')
    ns = SimpleNamespace(payload=user_id)
    data = getattr(ns, 'payload')
    def _primary():
        requests.get(str(data))
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return {"updated": True}
