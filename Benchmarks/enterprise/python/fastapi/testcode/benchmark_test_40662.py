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

async def BenchmarkTest40662(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = handle(upload_name)
    os.remove(str(data))
    return {"updated": True}
