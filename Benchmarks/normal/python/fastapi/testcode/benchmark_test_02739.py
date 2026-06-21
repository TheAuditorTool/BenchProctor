# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest02739(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = handle(auth_header)
    processed = data[:64]
    subprocess.Popen('echo ' + str(processed), shell=True).wait()
    return {"updated": True}
