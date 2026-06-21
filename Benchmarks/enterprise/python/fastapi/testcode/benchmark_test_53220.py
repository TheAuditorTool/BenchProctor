# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import boto3
from urllib.parse import unquote
from app_runtime import auth_check


async def BenchmarkTest53220(request: Request):
    path_value = request.path_params.get('id', '')
    data = unquote(path_value)
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return {"updated": True}
