# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest81456(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    if env_value:
        data = env_value
    else:
        data = ''
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
