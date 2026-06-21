# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess


async def BenchmarkTest16686(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    subprocess.run([str(env_value), '--status'], shell=False)
    return {"updated": True}
