# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import shlex
import os


async def BenchmarkTest41923(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    processed = shlex.quote(env_value)
    subprocess.run('echo ' + str(processed), shell=True)
    return {"updated": True}
