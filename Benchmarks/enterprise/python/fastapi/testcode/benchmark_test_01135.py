# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import jwt
import boto3


async def BenchmarkTest01135(request: Request):
    secret_value = 'default_setting_value'
    data = '{}'.format(secret_value)
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    jwt.encode({'sub': str(data)}, store_cred, algorithm='HS256')
    return {"updated": True}
