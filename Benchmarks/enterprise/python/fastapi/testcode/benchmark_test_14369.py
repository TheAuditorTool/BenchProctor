# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


def default_blank(value):
    return value if value is not None else ''
_shared_counter_lock = threading.Lock()

async def BenchmarkTest14369(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = default_blank(upload_name)
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
