# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import asyncio
import runpy


async def BenchmarkTest04656(request: Request):
    path_value = request.path_params.get('id', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return path_value
    data = await fetch_payload()
    async def _evasion_task():
        with open('plugins/generated_config.py', 'w') as fh:
            fh.write('SETTING = "' + str(data) + '"')
        runpy.run_path('plugins/generated_config.py')
    await _evasion_task()
    return {"updated": True}
