# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import base64
from starlette.responses import JSONResponse
import subprocess


async def BenchmarkTest30747(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    if data not in ('ls', 'cat', 'date', 'whoami'):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    processed = data
    subprocess.run([str(processed), '--status'], shell=False)
    return {"updated": True}
