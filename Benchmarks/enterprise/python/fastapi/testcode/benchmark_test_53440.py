# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
from fastapi import Form


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest53440(request: Request, field: str = Form('')):
    field_value = field
    data = handle(field_value)
    processed = data[:64]
    subprocess.run('echo ' + str(processed), shell=True)
    return {"updated": True}
