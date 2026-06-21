# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import jwt
import yaml
import asyncio


async def BenchmarkTest47244(request: Request):
    secret_value = 'feature_flag_value'
    async def fetch_payload():
        await asyncio.sleep(0)
        return secret_value
    data = await fetch_payload()
    with open('/etc/app/secrets.yaml') as f:
        store_cred = yaml.safe_load(f)['secret']
    jwt.encode({'sub': str(data)}, store_cred, algorithm='HS256')
    return {"updated": True}
