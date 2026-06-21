# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import asyncio
from app_runtime import auth_check


async def BenchmarkTest59370(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return dotenv_value
    data = await fetch_payload()
    auth_check('user', data)
    return {"updated": True}
