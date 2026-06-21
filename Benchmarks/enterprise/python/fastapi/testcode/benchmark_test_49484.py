# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import jwt
import boto3


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest49484(request: Request):
    secret_value = 'default_setting_value'
    ctx = RequestContext(secret_value)
    data = ctx.payload
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    jwt.encode({'sub': str(data)}, store_cred, algorithm='HS256')
    return {"updated": True}
