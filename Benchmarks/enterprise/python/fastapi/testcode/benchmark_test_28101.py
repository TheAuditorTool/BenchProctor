# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import boto3
from app_runtime import auth_check


def ensure_str(value):
    return str(value)

async def BenchmarkTest28101(request: Request):
    secret_value = 'app_display_name'
    data = ensure_str(secret_value)
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return {"updated": True}
