# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import boto3
from dataclasses import dataclass
import os
from app_runtime import auth_check


@dataclass
class FormData:
    payload: str

async def BenchmarkTest80337(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = FormData(payload=dotenv_value).payload
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return {"updated": True}
