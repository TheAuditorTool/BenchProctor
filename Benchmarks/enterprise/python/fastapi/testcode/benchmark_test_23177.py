# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import boto3
from dataclasses import dataclass
from fastapi import Form
from app_runtime import auth_check


@dataclass
class FormData:
    payload: str

async def BenchmarkTest23177(request: Request, field: str = Form('')):
    field_value = field
    data = FormData(payload=field_value).payload
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return {"updated": True}
