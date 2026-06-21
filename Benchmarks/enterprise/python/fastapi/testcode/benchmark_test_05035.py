# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import boto3
import os
import asyncio
from app_runtime import auth_check


async def BenchmarkTest05035(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return env_value
    data = await fetch_payload()
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return {"updated": True}
