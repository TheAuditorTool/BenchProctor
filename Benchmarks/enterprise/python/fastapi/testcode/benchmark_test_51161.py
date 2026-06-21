# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


_shared_counter_lock = threading.Lock()

async def BenchmarkTest51161(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    pending = list(str(header_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
