# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest15991(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = handle(upload_name)
    checked_path = os.path.normpath(data)
    with open('/var/app/data/' + str(checked_path), 'w') as fh:
        fh.write('data')
    return {"updated": True}
