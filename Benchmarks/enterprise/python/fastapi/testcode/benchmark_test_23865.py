# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import boto3
from app_runtime import auth_check


async def BenchmarkTest23865(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = ' '.join(str(header_value).split())
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return {"updated": True}
