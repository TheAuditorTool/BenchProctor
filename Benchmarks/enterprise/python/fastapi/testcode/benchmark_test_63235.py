# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import boto3
from types import SimpleNamespace
from app_runtime import auth_check


async def BenchmarkTest63235(request: Request):
    secret_value = 'default_setting_value'
    ns = SimpleNamespace(payload=secret_value)
    data = getattr(ns, 'payload')
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return {"updated": True}
