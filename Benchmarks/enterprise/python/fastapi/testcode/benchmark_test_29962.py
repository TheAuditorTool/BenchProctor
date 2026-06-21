# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import boto3
from app_runtime import auth_check


request_state: dict[str, str] = {}

async def BenchmarkTest29962(request: Request):
    secret_value = 'app_display_name'
    request_state['last_input'] = secret_value
    data = request_state['last_input']
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return {"updated": True}
