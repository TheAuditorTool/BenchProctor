# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import boto3
import asyncio
from app_runtime import auth_check


async def BenchmarkTest04267(request: Request):
    secret_value = 'feature_flag_value'
    async def fetch_payload():
        await asyncio.sleep(0)
        return secret_value
    data = await fetch_payload()
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return {"updated": True}
