# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
import os


_shared_counter_lock = threading.Lock()

async def BenchmarkTest59932(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data, _sep, _rest = str(env_value).partition('\x00')
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
