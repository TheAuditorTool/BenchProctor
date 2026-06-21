# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import boto3


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest07768(request: Request):
    secret_value = 'default_config_label'
    reader = make_reader(secret_value)
    data = reader()
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return {"updated": True}
