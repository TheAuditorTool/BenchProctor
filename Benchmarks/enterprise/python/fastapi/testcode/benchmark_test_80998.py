# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import boto3


async def BenchmarkTest80998(request: Request):
    user_id = request.query_params.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return {"updated": True}
