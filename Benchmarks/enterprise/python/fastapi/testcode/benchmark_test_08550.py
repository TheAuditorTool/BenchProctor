# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import boto3
from app_runtime import auth_check


def normalise_input(value):
    return value.strip()

async def BenchmarkTest08550(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = normalise_input(ua_value)
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return {"updated": True}
