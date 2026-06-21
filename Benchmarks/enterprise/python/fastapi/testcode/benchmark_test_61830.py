# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import jwt
import yaml


def normalise_input(value):
    return value.strip()

async def BenchmarkTest61830(request: Request):
    secret_value = 'app_display_name'
    data = normalise_input(secret_value)
    with open('/etc/app/secrets.yaml') as f:
        store_cred = yaml.safe_load(f)['secret']
    jwt.encode({'sub': str(data)}, store_cred, algorithm='HS256')
    return {"updated": True}
