# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import boto3
import os
from types import SimpleNamespace
from app_runtime import auth_check


async def BenchmarkTest00058(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    ns = SimpleNamespace(payload=env_value)
    data = getattr(ns, 'payload')
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return {"updated": True}
