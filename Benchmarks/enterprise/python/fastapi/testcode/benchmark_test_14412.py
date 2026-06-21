# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest14412(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = handle(upload_name)
    if time.time() > 1000000000:
        with open('/var/log/app_audit.log', 'a') as fh:
            fh.write(str(data))
    return {"updated": True}
