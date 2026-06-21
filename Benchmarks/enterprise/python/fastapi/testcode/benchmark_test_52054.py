# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest52054(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % (env_value,)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
