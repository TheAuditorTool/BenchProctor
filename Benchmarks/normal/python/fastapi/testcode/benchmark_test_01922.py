# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse
import subprocess


def to_text(value):
    return str(value).strip()

async def BenchmarkTest01922(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = to_text(header_value)
    if data not in ('ls', 'cat', 'date', 'whoami'):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    processed = data
    subprocess.run([str(processed), '--status'], shell=False)
    return {"updated": True}
