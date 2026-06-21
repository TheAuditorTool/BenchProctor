# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import boto3
import json
from app_runtime import auth_check


async def BenchmarkTest65190(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return {"updated": True}
