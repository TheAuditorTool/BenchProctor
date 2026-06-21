# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import boto3
from app_runtime import auth_check


def relay_value(value):
    return value

async def BenchmarkTest74326(request: Request):
    secret_value = 'feature_flag_value'
    data = relay_value(secret_value)
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return {"updated": True}
