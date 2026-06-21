# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
import os


_shared_counter_lock = threading.Lock()

async def BenchmarkTest07069(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    pending = list(str(env_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
