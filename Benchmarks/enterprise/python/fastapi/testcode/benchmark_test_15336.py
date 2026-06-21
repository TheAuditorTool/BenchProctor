# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import os


async def BenchmarkTest15336(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data, _sep, _rest = str(env_value).partition('\x00')
    subprocess.run('echo ' + str(data), shell=True)
    return {"updated": True}
