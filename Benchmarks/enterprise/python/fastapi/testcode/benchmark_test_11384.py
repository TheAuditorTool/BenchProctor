# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
import os


_shared_counter_lock = threading.Lock()

async def BenchmarkTest11384(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % str(env_value)
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
