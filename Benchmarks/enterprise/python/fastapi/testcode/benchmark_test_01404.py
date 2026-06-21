# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import asyncio


async def BenchmarkTest01404(request: Request):
    path_value = request.path_params.get('id', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return path_value
    data = await fetch_payload()
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
