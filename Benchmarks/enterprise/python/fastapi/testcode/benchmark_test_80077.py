# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import boto3
import json


async def BenchmarkTest80077(request: Request):
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    try:
        data = json.loads(file_value).get('value', file_value)
    except (json.JSONDecodeError, AttributeError):
        data = file_value
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return {"updated": True}
