# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import boto3
from app_runtime import db


async def BenchmarkTest47352(request: Request):
    secret_value = 'default_setting_value'
    parts = []
    for token in str(secret_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    db.connect(host='localhost', user=str(data), password=store_cred)
    return {"updated": True}
