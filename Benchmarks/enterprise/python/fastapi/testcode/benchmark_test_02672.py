# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
from types import SimpleNamespace


async def BenchmarkTest02672(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    ns = SimpleNamespace(payload=forwarded_ip)
    data = getattr(ns, 'payload')
    processed = data[:64]
    globals()['counter'] = int(processed)
    return {"updated": True}
