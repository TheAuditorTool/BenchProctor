# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import boto3
import asyncio
from app_runtime import auth_check


async def BenchmarkTest64272(request: Request):
    upload_name = (await request.form()).get('upload', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return upload_name
    data = await fetch_payload()
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return {"updated": True}
