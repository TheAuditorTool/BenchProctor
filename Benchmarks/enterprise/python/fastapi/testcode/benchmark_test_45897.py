# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest45897(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    with open('output.csv', 'a') as fh:
        fh.write(str(env_value) + ',data\n')
    return {"updated": True}
