# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import boto3
from app_runtime import db


async def BenchmarkTest73054(request: Request):
    secret_value = 'app_display_name'
    data = f'{secret_value:.200s}'
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    db.connect(host='localhost', user=str(data), password=store_cred)
    return {"updated": True}
