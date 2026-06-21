# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


def coalesce_blank(value):
    return value or ''
_shared_counter_lock = threading.Lock()

async def BenchmarkTest44407(request: Request):
    path_value = request.path_params.get('id', '')
    data = coalesce_blank(path_value)
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
