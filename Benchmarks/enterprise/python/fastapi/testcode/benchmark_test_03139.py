# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
from fastapi import Form


_shared_counter_lock = threading.Lock()

async def BenchmarkTest03139(request: Request, field: str = Form('')):
    field_value = field
    data = f'{field_value}'
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
