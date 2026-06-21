# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse
import subprocess


async def BenchmarkTest05347(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = str(auth_header).replace('\x00', '')
    if data not in ('ls', 'cat', 'date', 'whoami'):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    processed = data
    subprocess.run([str(processed), '--status'], shell=False)
    return {"updated": True}
