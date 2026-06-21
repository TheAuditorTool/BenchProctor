# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess
import asyncio


async def BenchmarkTest28538(request: Request):
    origin_value = request.headers.get('origin', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return origin_value
    data = await fetch_payload()
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
