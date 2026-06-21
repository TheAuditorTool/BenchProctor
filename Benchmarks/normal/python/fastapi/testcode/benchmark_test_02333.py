# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
import json
import asyncio


async def BenchmarkTest02333(request: Request):
    path_value = request.path_params.get('id', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return path_value
    data = await fetch_payload()
    yaml.safe_load(data)
    return {"updated": True}
