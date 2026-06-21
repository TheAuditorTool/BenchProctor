# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import jwt
import os
import asyncio


async def BenchmarkTest13195(request: Request):
    secret_value = 'feature_flag_value'
    async def fetch_payload():
        await asyncio.sleep(0)
        return secret_value
    data = await fetch_payload()
    store_cred = os.environ.get('APP_SECRET', '')
    jwt.encode({'sub': str(data)}, store_cred, algorithm='HS256')
    return {"updated": True}
