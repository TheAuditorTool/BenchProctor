# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
from types import SimpleNamespace


_shared_counter_lock = threading.Lock()

async def BenchmarkTest02929(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    ns = SimpleNamespace(payload=raw_body)
    data = getattr(ns, 'payload')
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
