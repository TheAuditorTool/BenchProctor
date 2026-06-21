# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import asyncio
from app_runtime import auth_check


async def BenchmarkTest12482(request: Request):
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    async def fetch_payload():
        await asyncio.sleep(0)
        return secret_value
    data = await fetch_payload()
    auth_check('user', data)
    return {"updated": True}
