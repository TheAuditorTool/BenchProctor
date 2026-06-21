# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import boto3
import base64
from app_runtime import auth_check


async def BenchmarkTest16812(request: Request):
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    data = base64.b64decode(file_value).decode('utf-8', 'ignore')
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return {"updated": True}
