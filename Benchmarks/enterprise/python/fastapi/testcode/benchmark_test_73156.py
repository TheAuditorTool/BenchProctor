# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
from fastapi import Form


_shared_counter_lock = threading.Lock()

async def BenchmarkTest73156(request: Request, field: str = Form('')):
    field_value = field
    data, _sep, _rest = str(field_value).partition('\x00')
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
