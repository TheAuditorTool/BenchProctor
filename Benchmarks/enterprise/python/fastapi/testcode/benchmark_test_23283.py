# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import boto3
from dataclasses import dataclass
from app_runtime import auth_check


@dataclass
class FormData:
    payload: str

async def BenchmarkTest23283(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = FormData(payload=cookie_value).payload
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return {"updated": True}
