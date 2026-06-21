# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import boto3
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest30213(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    ctx = RequestContext(dotenv_value)
    data = ctx.payload
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return {"updated": True}
