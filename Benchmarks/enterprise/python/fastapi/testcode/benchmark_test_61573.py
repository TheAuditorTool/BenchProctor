# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import boto3
import os
from app_runtime import auth_check


async def BenchmarkTest61573(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    parts = str(dotenv_value).split(',')
    data = ','.join(parts)
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return {"updated": True}
