# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


_shared_counter_lock = threading.Lock()

async def BenchmarkTest36575(request: Request):
    auth_header = request.headers.get('authorization', '')
    kind = 'json' if str(auth_header).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = auth_header
            data = parsed
        case _:
            data = auth_header
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
