# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import sys
from starlette.responses import JSONResponse


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest06048(request: Request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    data = handle(argv_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    subprocess.Popen('echo ' + str(processed), shell=True).wait()
    return {"updated": True}
