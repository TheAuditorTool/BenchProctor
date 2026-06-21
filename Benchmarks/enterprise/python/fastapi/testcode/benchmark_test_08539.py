# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import boto3
from fastapi import Form
from app_runtime import auth_check


async def BenchmarkTest08539(request: Request, field: str = Form('')):
    field_value = field
    data = field_value if field_value else 'default'
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return {"updated": True}
