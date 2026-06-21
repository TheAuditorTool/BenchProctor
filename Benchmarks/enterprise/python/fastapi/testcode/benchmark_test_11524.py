# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
from fastapi import Form


_shared_counter_lock = threading.Lock()

async def BenchmarkTest11524(request: Request, field: str = Form('')):
    field_value = field
    data = str(field_value).replace('\x00', '')
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
