# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest03059(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    prefix = ''
    data = prefix + str(env_value)
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return {"updated": True}
