# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import jwt
import boto3


async def BenchmarkTest59515(request: Request):
    secret_value = 'app_display_name'
    data = (lambda v: v.strip())(secret_value)
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    jwt.encode({'sub': str(data)}, store_cred, algorithm='HS256')
    return {"updated": True}
