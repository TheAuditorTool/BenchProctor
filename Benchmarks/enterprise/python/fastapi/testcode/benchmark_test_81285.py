# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest81285(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    parts = str(env_value).split(',')
    data = ','.join(parts)
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return {"updated": True}
