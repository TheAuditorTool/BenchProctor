# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import boto3
import asyncio
from app_runtime import auth_check


async def BenchmarkTest30668(request: Request):
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    async def fetch_payload():
        await asyncio.sleep(0)
        return file_value
    data = await fetch_payload()
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return {"updated": True}
