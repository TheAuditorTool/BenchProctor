# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from dataclasses import dataclass
import os


@dataclass
class FormData:
    payload: str

async def BenchmarkTest02655(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(digest)
    return {"updated": True}
