# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


def make_reader(raw):
    def read():
        return raw.strip()
    return read
_shared_counter_lock = threading.Lock()

async def BenchmarkTest74017(request: Request):
    origin_value = request.headers.get('origin', '')
    reader = make_reader(origin_value)
    data = reader()
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
