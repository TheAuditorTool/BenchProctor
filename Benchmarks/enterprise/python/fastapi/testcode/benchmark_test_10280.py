# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import boto3


async def BenchmarkTest10280(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data, _sep, _rest = str(ua_value).partition('\x00')
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return {"updated": True}
