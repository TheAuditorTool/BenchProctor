# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
import os


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest03331(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = coalesce_blank(env_value)
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(digest)
    return {"updated": True}
