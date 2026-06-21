# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
import os


def to_text(value):
    return str(value).strip()

async def BenchmarkTest03236(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = to_text(env_value)
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(digest)
    return {"updated": True}
