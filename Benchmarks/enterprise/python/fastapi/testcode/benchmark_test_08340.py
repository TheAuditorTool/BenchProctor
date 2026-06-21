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

async def BenchmarkTest08340(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = handle(auth_header)
    def _primary():
        subprocess.Popen('echo ' + str(data), shell=True).wait()
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return {"updated": True}
