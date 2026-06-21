# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
from urllib.parse import unquote
from starlette.responses import JSONResponse


async def BenchmarkTest36371(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    if data not in ('ls', 'cat', 'date', 'whoami'):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    processed = data
    subprocess.run('echo ' + str(processed), shell=True)
    return {"updated": True}
