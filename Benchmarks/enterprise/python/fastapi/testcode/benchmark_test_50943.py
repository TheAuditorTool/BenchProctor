# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import re
from starlette.responses import JSONResponse
import subprocess


def ensure_str(value):
    return str(value)

async def BenchmarkTest50943(request: Request):
    host_value = request.headers.get('host', '')
    data = ensure_str(host_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    subprocess.run([str(processed), '--status'], shell=False)
    return {"updated": True}
