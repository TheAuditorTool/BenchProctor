# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import boto3
from app_runtime import db


async def BenchmarkTest12340(request: Request):
    secret_value = 'feature_flag_value'
    if secret_value:
        data = secret_value
    else:
        data = ''
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    db.connect(host='localhost', user=str(data), password=store_cred)
    return {"updated": True}
