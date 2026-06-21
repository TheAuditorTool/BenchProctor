# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


_shared_counter_lock = threading.Lock()

async def BenchmarkTest33514(request: Request):
    host_value = request.headers.get('host', '')
    kind = 'json' if str(host_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = host_value
            data = parsed
        case _:
            data = host_value
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
