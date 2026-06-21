# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str
_shared_counter_lock = threading.Lock()

async def BenchmarkTest43458(request: Request):
    path_value = request.path_params.get('id', '')
    data = FormData(payload=path_value).payload
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
