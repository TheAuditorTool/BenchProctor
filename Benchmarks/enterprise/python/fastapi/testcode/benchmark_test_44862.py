# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import jwt
import yaml


async def BenchmarkTest44862(request: Request):
    secret_value = 'default_setting_value'
    parts = str(secret_value).split(',')
    data = ','.join(parts)
    with open('/etc/app/secrets.yaml') as f:
        store_cred = yaml.safe_load(f)['secret']
    jwt.encode({'sub': str(data)}, store_cred, algorithm='HS256')
    return {"updated": True}
