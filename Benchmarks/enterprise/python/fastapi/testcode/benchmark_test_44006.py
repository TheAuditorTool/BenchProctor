# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import re
import sys
from starlette.responses import JSONResponse
from types import SimpleNamespace


async def BenchmarkTest44006(request: Request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    ns = SimpleNamespace(payload=argv_value)
    data = getattr(ns, 'payload')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    subprocess.Popen('echo ' + str(processed), shell=True).wait()
    return {"updated": True}
