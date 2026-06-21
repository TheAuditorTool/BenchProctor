# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


_shared_counter_lock = threading.Lock()

async def BenchmarkTest27706(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = xml_value.decode('utf-8', 'ignore') if isinstance(xml_value, bytes) else xml_value
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
