# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
import json
from types import SimpleNamespace


_shared_counter_lock = threading.Lock()

async def BenchmarkTest54382(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    ns = SimpleNamespace(payload=graphql_var)
    data = getattr(ns, 'payload')
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
