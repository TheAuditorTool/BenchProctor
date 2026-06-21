# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import boto3
from fastapi import Form
from app_runtime import auth_check


async def BenchmarkTest62612(request: Request, field: str = Form('')):
    field_value = field
    parts = []
    for token in str(field_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return {"updated": True}
