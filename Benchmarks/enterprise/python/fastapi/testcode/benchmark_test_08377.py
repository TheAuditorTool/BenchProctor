# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess


async def BenchmarkTest08377(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value}'
    subprocess.run([str(data), '--status'], shell=False)
    return {"updated": True}
