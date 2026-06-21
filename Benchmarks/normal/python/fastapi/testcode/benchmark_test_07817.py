# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import asyncio


async def BenchmarkTest07817(request: Request):
    path_value = request.path_params.get('id', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return path_value
    data = await fetch_payload()
    processed = data[:64]
    data = bytearray(int(processed) if str(processed).isdigit() else 0)
    return {"updated": True}
