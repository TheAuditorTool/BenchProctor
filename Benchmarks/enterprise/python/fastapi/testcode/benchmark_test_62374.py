# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import boto3
from app_runtime import auth_check


async def BenchmarkTest62374(request: Request):
    host_value = request.headers.get('host', '')
    data, _sep, _rest = str(host_value).partition('\x00')
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return {"updated": True}
