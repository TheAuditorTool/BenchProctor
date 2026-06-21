# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import os


async def BenchmarkTest45942(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    subprocess.run('echo ' + str(env_value), shell=True)
    return {"updated": True}
