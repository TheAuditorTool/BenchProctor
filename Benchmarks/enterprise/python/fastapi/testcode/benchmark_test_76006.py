# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import re
from urllib.parse import unquote
from starlette.responses import JSONResponse


async def BenchmarkTest76006(request: Request):
    referer_value = request.headers.get('referer', '')
    data = unquote(referer_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    subprocess.Popen('echo ' + str(processed), shell=True).wait()
    return {"updated": True}
