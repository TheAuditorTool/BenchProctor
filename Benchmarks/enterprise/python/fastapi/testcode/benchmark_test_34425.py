# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import jwt
import boto3


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest34425(request: Request):
    secret_value = 'feature_flag_value'
    data = RequestPayload(secret_value).value
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    jwt.encode({'sub': str(data)}, store_cred, algorithm='HS256')
    return {"updated": True}
