# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse
import subprocess


async def BenchmarkTest71867(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    if forwarded_ip not in ('ls', 'cat', 'date', 'whoami'):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    processed = forwarded_ip
    subprocess.run([str(processed), '--status'], shell=False)
    return {"updated": True}
