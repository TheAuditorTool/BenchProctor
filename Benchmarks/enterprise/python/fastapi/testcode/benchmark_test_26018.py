# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import asyncio
from app_runtime import ssm_client


async def BenchmarkTest26018(request: Request):
    ssm_value = ssm_client.get_parameter(Name='/app/secret')['Parameter']['Value']
    async def fetch_payload():
        await asyncio.sleep(0)
        return ssm_value
    data = await fetch_payload()
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return {"updated": True}
