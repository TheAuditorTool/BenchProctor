# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from types import SimpleNamespace
import pickle


async def BenchmarkTest13807(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    ns = SimpleNamespace(payload=forwarded_ip)
    data = getattr(ns, 'payload')
    def _primary():
        pickle.loads(data.encode('latin-1'))
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return {"updated": True}
