# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import boto3
from app_runtime import auth_check


async def BenchmarkTest48618(request: Request):
    secret_value = 'default_setting_value'
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(secret_value), store_cred)
    return {"updated": True}
