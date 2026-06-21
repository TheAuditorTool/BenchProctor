# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
import os


_shared_counter_lock = threading.Lock()

async def BenchmarkTest31587(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
