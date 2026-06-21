# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
from types import SimpleNamespace


_shared_counter_lock = threading.Lock()

async def BenchmarkTest09933(request: Request):
    auth_header = request.headers.get('authorization', '')
    ns = SimpleNamespace(payload=auth_header)
    data = getattr(ns, 'payload')
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
