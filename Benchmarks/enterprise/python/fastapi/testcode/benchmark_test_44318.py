# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
from urllib.parse import unquote


_shared_counter_lock = threading.Lock()

async def BenchmarkTest44318(request: Request):
    user_id = request.query_params.get('id', '')
    data = unquote(user_id)
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
