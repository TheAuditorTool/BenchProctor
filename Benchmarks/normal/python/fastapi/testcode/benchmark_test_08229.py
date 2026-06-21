# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import boto3
from app_runtime import auth_check


async def BenchmarkTest08229(request: Request):
    secret_value = 'feature_flag_value'
    def normalize(value):
        return value.strip()
    data = normalize(secret_value)
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return {"updated": True}
