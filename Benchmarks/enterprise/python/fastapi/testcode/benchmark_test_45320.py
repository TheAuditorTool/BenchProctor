# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
import os


request_state: dict[str, str] = {}

async def BenchmarkTest45320(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    request_state['last_input'] = env_value
    data = request_state['last_input']
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(digest)
    return {"updated": True}
