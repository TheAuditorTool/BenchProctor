# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import boto3
from app_runtime import auth_check


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest02611(request: Request):
    secret_value = 'default_setting_value'
    data = coalesce_blank(secret_value)
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return {"updated": True}
