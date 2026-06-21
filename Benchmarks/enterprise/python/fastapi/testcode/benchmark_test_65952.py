# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


def make_reader(raw):
    def read():
        return raw.strip()
    return read
_shared_counter_lock = threading.Lock()

async def BenchmarkTest65952(request: Request):
    upload_name = (await request.form()).get('upload', '')
    reader = make_reader(upload_name)
    data = reader()
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
