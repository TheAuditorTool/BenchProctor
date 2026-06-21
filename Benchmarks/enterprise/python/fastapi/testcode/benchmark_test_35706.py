# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import boto3
from app_runtime import auth_check


def normalise_input(value):
    return value.strip()

async def BenchmarkTest35706(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = normalise_input(cookie_value)
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return {"updated": True}
