# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import boto3
import base64
from app_runtime import auth_check


async def BenchmarkTest76556(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return {"updated": True}
