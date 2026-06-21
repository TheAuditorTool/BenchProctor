# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


def make_reader(raw):
    def read():
        return raw.strip()
    return read
_shared_counter_lock = threading.Lock()

async def BenchmarkTest53063(request: Request):
    path_value = request.path_params.get('id', '')
    reader = make_reader(path_value)
    data = reader()
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
