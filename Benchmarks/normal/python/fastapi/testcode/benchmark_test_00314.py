# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import boto3
from app_runtime import auth_check


def to_text(value):
    return str(value).strip()

async def BenchmarkTest00314(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = to_text(xml_value)
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return {"updated": True}
