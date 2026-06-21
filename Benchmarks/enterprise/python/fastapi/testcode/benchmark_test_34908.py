# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import boto3
import json
from app_runtime import db


async def BenchmarkTest34908(request: Request):
    secret_value = 'default_config_label'
    try:
        data = json.loads(secret_value).get('value', secret_value)
    except (json.JSONDecodeError, AttributeError):
        data = secret_value
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    db.connect(host='localhost', user=str(data), password=store_cred)
    return {"updated": True}
