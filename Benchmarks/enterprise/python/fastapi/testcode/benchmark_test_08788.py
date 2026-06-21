# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from types import SimpleNamespace


async def BenchmarkTest08788(request: Request):
    referer_value = request.headers.get('referer', '')
    ns = SimpleNamespace(payload=referer_value)
    data = getattr(ns, 'payload')
    processed = data[:64]
    request.session['data'] = str(processed)
    return {"updated": True}
