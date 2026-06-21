# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
from fastapi import Form


_shared_counter_lock = threading.Lock()

async def BenchmarkTest54484(request: Request, field: str = Form('')):
    field_value = field
    pending = list(str(field_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
