# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import os
from starlette.responses import JSONResponse


async def BenchmarkTest00835(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data, _sep, _rest = str(env_value).partition('\x00')
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    subprocess.Popen('echo ' + str(processed), shell=True).wait()
    return {"updated": True}
