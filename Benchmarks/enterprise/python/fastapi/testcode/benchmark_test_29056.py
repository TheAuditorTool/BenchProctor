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

async def BenchmarkTest29056(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = handle(upload_name)
    if os.environ.get("APP_ENV", "production") != "test":
        eval(str(data))
    return {"updated": True}
