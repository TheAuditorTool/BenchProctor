# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import boto3
from urllib.parse import unquote
from app_runtime import auth_check


async def BenchmarkTest57463(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return {"updated": True}
