# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from urllib.parse import unquote
from starlette.responses import JSONResponse
import subprocess


async def BenchmarkTest12454(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    if data not in ('ls', 'cat', 'date', 'whoami'):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    processed = data
    subprocess.run([str(processed), '--status'], shell=False)
    return {"updated": True}
