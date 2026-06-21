# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
import os


_shared_counter_lock = threading.Lock()

async def BenchmarkTest38831(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    with _shared_counter_lock:
        globals()['counter'] = int(env_value)
    return {"updated": True}
