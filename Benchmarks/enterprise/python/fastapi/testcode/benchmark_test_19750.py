# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import re
from starlette.responses import JSONResponse
import subprocess


async def BenchmarkTest19750(request: Request):
    origin_value = request.headers.get('origin', '')
    if origin_value:
        data = origin_value
    else:
        data = ''
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    subprocess.run([str(processed), '--status'], shell=False)
    return {"updated": True}
