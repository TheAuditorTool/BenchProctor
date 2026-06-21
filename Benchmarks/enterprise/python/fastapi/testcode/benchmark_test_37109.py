# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import asyncio
import defusedxml.ElementTree


async def BenchmarkTest37109(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return env_value
    data = await fetch_payload()
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
