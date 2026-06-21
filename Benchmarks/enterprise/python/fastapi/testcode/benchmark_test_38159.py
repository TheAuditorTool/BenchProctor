# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import boto3
from fastapi import Form
import asyncio
from app_runtime import auth_check


async def BenchmarkTest38159(request: Request, field: str = Form('')):
    field_value = field
    async def fetch_payload():
        await asyncio.sleep(0)
        return field_value
    data = await fetch_payload()
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return {"updated": True}
