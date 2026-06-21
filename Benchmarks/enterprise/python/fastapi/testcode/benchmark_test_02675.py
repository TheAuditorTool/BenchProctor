# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import os


async def BenchmarkTest02675(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    def normalize(value):
        return value.strip()
    data = normalize(env_value)
    subprocess.run('echo ' + str(data), shell=True)
    return {"updated": True}
