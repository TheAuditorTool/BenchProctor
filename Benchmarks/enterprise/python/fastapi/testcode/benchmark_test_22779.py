# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import boto3
import os
from app_runtime import auth_check


async def BenchmarkTest22779(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = '%s' % str(dotenv_value)
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return {"updated": True}
