# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import boto3


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest69523(request: Request):
    secret_value = 'feature_flag_value'
    data = coalesce_blank(secret_value)
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return {"updated": True}
