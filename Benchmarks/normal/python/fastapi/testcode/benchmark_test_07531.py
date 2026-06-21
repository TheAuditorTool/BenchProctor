# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import os


async def BenchmarkTest07531(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return {"updated": True}
