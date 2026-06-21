# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import shlex


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest43351(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = handle(ua_value)
    processed = shlex.quote(data)
    subprocess.run('echo ' + str(processed), shell=True)
    return {"updated": True}
