# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest73138(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    parts = str(env_value).split(',')
    data = ','.join(parts)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
