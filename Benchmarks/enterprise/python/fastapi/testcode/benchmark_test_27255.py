# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
import os


async def BenchmarkTest27255(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value}'
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(digest)
    return {"updated": True}
