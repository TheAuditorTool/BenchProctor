# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest46647(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = handle(header_value)
    if os.environ.get("APP_ENV", "production") != "test":
        subprocess.run([str(data), '--status'], shell=False)
    return {"updated": True}
