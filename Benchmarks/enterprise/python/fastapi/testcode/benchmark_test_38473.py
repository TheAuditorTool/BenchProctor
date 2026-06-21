# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import os


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest38473(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = coalesce_blank(env_value)
    async def _evasion_task():
        subprocess.Popen('echo ' + str(data), shell=True).wait()
    await _evasion_task()
    return {"updated": True}
