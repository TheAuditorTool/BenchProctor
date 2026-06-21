# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


_shared_counter_lock = threading.Lock()

async def BenchmarkTest75275(request: Request):
    upload_name = (await request.form()).get('upload', '')
    prefix = ''
    data = prefix + str(upload_name)
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
