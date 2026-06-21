# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import boto3
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest51034(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = FormData(payload=auth_header).payload
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return {"updated": True}
