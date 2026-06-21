# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
from dataclasses import dataclass
import os


@dataclass
class FormData:
    payload: str
_shared_counter_lock = threading.Lock()

async def BenchmarkTest24168(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
