# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import re
from starlette.responses import JSONResponse


async def BenchmarkTest48360(request: Request):
    referer_value = request.headers.get('referer', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(referer_value)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = referer_value
    subprocess.Popen('echo ' + str(processed), shell=True).wait()
    return {"updated": True}
