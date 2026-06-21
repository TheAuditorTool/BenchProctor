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

async def BenchmarkTest40458(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = handle(header_value)
    eval(compile("subprocess.Popen('echo ' + str(data), shell=True).wait()", '<sink>', 'exec'))
    return {"updated": True}
