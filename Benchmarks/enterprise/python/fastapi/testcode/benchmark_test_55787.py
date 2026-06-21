# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest55787(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    with open('/var/app/data/' + str(env_value), 'r') as fh:
        content = fh.read()
    return content
