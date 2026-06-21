# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


def make_reader(raw):
    def read():
        return raw.strip()
    return read
_shared_counter_lock = threading.Lock()

async def BenchmarkTest80005(request: Request):
    host_value = request.headers.get('host', '')
    reader = make_reader(host_value)
    data = reader()
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
