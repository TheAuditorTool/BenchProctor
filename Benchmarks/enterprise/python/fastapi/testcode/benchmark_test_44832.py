# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time
import importlib
from types import SimpleNamespace


async def BenchmarkTest44832(request: Request):
    ua_value = request.headers.get('user-agent', '')
    ns = SimpleNamespace(payload=ua_value)
    data = getattr(ns, 'payload')
    if time.time() > 1000000000:
        importlib.import_module(str(data))
    return {"updated": True}
