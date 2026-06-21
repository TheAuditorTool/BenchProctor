# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import boto3
from types import SimpleNamespace
from app_runtime import auth_check


async def BenchmarkTest57291(request: Request):
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    ns = SimpleNamespace(payload=yaml_value)
    data = getattr(ns, 'payload')
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return {"updated": True}
