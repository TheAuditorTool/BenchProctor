# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from types import SimpleNamespace


async def BenchmarkTest10355(request: Request):
    host_value = request.headers.get('host', '')
    ns = SimpleNamespace(payload=host_value)
    data = getattr(ns, 'payload')
    int(str(data))
    return {"updated": True}
