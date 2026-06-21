# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
import os


_shared_counter_lock = threading.Lock()

async def BenchmarkTest02436(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    if env_value:
        data = env_value
    else:
        data = ''
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
