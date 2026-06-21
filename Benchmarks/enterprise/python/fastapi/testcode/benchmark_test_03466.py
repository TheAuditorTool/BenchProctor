# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from types import SimpleNamespace


async def BenchmarkTest03466(request: Request):
    referer_value = request.headers.get('referer', '')
    ns = SimpleNamespace(payload=referer_value)
    data = getattr(ns, 'payload')
    processed = data[:64]
    data = bytearray(int(processed) if str(processed).isdigit() else 0)
    return {"updated": True}
