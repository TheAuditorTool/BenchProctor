# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest11512(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
