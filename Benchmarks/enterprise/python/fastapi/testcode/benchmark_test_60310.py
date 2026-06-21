# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest60310(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value}'
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
