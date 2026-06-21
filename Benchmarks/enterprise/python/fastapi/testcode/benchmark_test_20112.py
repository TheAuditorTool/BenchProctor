# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import re
import os
from starlette.responses import JSONResponse


def normalise_input(value):
    return value.strip()

async def BenchmarkTest20112(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = normalise_input(env_value)
    if not re.fullmatch('^[\\w\\s.;|&$`\'\\"_/\\-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    subprocess.run('echo ' + str(processed), shell=True)
    return {"updated": True}
