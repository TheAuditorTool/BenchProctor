# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import boto3
from fastapi import Form
from app_runtime import auth_check


async def BenchmarkTest74052(request: Request, field: str = Form('')):
    field_value = field
    data = '%s' % str(field_value)
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return {"updated": True}
