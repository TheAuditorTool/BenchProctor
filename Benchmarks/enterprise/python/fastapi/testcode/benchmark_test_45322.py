# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import re
from urllib.parse import unquote
from starlette.responses import JSONResponse


async def BenchmarkTest45322(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    subprocess.Popen('echo ' + str(processed), shell=True).wait()
    return {"updated": True}
