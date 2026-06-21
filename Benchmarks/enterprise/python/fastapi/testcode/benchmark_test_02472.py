# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import boto3
import json
from app_runtime import auth_check


async def BenchmarkTest02472(request: Request):
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    data = json.loads(yaml_value).get('value', '')
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return {"updated": True}
