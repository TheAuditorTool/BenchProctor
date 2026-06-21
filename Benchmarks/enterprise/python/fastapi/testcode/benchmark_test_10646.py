# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import asyncio
from app_runtime import auth_check


async def BenchmarkTest10646(request: Request):
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    async def fetch_payload():
        await asyncio.sleep(0)
        return file_value
    data = await fetch_payload()
    auth_check('user', data)
    return {"updated": True}
