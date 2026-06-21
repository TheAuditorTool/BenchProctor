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

async def BenchmarkTest37260(request: Request, field: str = Form('')):
    field_value = field
    data = handle(field_value)
    processed = data[:64]
    subprocess.Popen('echo ' + str(processed), shell=True).wait()
    return {"updated": True}
