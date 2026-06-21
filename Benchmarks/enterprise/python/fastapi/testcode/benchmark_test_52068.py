# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import asyncio
import tempfile


async def BenchmarkTest52068(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return env_value
    data = await fetch_payload()
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
