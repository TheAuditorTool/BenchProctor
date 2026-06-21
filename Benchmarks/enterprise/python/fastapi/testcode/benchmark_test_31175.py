# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest31175(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    if env_value:
        data = env_value
    else:
        data = ''
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
