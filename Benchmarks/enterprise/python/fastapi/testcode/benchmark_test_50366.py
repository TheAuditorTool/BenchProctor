# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import re
import os
from starlette.responses import JSONResponse


async def BenchmarkTest50366(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(env_value)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = env_value
    subprocess.run('echo ' + str(processed), shell=True)
    return {"updated": True}
