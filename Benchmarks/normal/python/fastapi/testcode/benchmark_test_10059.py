# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
import os


async def BenchmarkTest10059(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(digest)
    return {"updated": True}
