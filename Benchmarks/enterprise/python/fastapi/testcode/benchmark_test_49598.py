# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import os


async def BenchmarkTest49598(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    parts = str(env_value).split(',')
    data = ','.join(parts)
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return {"updated": True}
