# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


_shared_counter_lock = threading.Lock()

async def BenchmarkTest51501(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    parts = []
    for token in str(multipart_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
