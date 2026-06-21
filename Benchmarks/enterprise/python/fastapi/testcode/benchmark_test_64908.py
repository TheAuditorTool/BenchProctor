# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest64908(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = '{}'.format(env_value)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
