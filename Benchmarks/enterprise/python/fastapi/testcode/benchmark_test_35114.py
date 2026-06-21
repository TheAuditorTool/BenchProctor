# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import boto3
import os


def to_text(value):
    return str(value).strip()

async def BenchmarkTest35114(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = to_text(dotenv_value)
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return {"updated": True}
