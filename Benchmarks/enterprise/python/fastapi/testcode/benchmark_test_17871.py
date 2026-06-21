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

async def BenchmarkTest17871(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = handle(ua_value)
    async def _evasion_task():
        subprocess.run([str(data), '--status'], shell=False)
    await _evasion_task()
    return {"updated": True}
