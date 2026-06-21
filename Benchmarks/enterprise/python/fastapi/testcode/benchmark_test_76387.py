# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import os
from starlette.responses import JSONResponse


async def BenchmarkTest76387(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    if env_value:
        data = env_value
    else:
        data = ''
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    subprocess.Popen('echo ' + str(processed), shell=True).wait()
    return {"updated": True}
