# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import os
from starlette.responses import JSONResponse


async def BenchmarkTest08640(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = '{}'.format(env_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    subprocess.run('echo ' + str(processed), shell=True)
    return {"updated": True}
