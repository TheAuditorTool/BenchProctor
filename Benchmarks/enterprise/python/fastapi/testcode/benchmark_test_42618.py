# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import jwt
import yaml
import asyncio


async def BenchmarkTest42618(request: Request):
    secret_value = 'default_setting_value'
    async def fetch_payload():
        await asyncio.sleep(0)
        return secret_value
    data = await fetch_payload()
    with open('/etc/app/secrets.yaml') as f:
        store_cred = yaml.safe_load(f)['secret']
    jwt.encode({'sub': str(data)}, store_cred, algorithm='HS256')
    return {"updated": True}
