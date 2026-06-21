# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import asyncio
import runpy


async def BenchmarkTest52658(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return env_value
    data = await fetch_payload()
    if os.environ.get("APP_ENV", "production") != "test":
        with open('plugins/generated_config.py', 'w') as fh:
            fh.write('SETTING = "' + str(data) + '"')
        runpy.run_path('plugins/generated_config.py')
    return {"updated": True}
