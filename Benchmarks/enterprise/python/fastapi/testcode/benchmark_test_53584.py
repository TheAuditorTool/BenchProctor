# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import shlex
import os


async def BenchmarkTest53584(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    if env_value:
        data = env_value
    else:
        data = ''
    processed = shlex.quote(data)
    subprocess.run('echo ' + str(processed), shell=True)
    return {"updated": True}
