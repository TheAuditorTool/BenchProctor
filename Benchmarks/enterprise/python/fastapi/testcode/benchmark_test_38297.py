# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import boto3


async def BenchmarkTest38297(request: Request):
    upload_name = (await request.form()).get('upload', '')
    prefix = ''
    data = prefix + str(upload_name)
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return {"updated": True}
