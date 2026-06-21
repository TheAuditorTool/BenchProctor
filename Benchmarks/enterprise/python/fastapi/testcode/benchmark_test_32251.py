# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import asyncio


async def BenchmarkTest32251(request: Request):
    path_value = request.path_params.get('id', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return path_value
    data = await fetch_payload()
    os.setuid(int(str(data)) if str(data).isdigit() else 0)
    return {"updated": True}
