# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import boto3
from dataclasses import dataclass
from app_runtime import auth_check


@dataclass
class FormData:
    payload: str

async def BenchmarkTest45680(request: Request):
    user_id = request.query_params.get('id', '')
    data = FormData(payload=user_id).payload
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return {"updated": True}
