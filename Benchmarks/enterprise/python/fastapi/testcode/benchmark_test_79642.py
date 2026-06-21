# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import re
from starlette.responses import JSONResponse


async def BenchmarkTest79642(request: Request):
    auth_header = request.headers.get('authorization', '')
    parts = str(auth_header).split(',')
    data = ','.join(parts)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = data
    subprocess.Popen('echo ' + str(processed), shell=True).wait()
    return {"updated": True}
