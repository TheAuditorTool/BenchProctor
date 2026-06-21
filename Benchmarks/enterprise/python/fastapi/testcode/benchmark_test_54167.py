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

async def BenchmarkTest54167(request: Request):
    host_value = request.headers.get('host', '')
    data = handle(host_value)
    async def _evasion_task():
        subprocess.run([str(data), '--status'], shell=False)
    await _evasion_task()
    return {"updated": True}
