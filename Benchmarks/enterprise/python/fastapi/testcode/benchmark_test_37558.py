# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from types import SimpleNamespace


async def BenchmarkTest37558(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    ns = SimpleNamespace(payload=forwarded_ip)
    data = getattr(ns, 'payload')
    processed = data[:64]
    request.session['data'] = str(processed)
    return {"updated": True}
