# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import asyncio
from app_runtime import auth_check


async def BenchmarkTest74727(request: Request):
    secret_value = 'config_secret_test_abc123'
    async def fetch_payload():
        await asyncio.sleep(0)
        return secret_value
    data = await fetch_payload()
    auth_check('user', data)
    return {"updated": True}
