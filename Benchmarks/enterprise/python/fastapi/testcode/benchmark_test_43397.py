# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import jwt
import asyncio


async def BenchmarkTest43397(request: Request):
    secret_value = 'config_secret_test_abc123'
    async def fetch_payload():
        await asyncio.sleep(0)
        return secret_value
    data = await fetch_payload()
    jwt.encode({'sub': 'user'}, data, algorithm='HS256')
    return {"updated": True}
