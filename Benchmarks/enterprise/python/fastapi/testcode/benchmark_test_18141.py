# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import re
import sys
from starlette.responses import JSONResponse


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest18141(request: Request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    data = handle(argv_value)
    if not re.fullmatch('^[\\w\\s.;|&$`\'\\"_/\\-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    os.system('echo ' + str(processed))
    return {"updated": True}
