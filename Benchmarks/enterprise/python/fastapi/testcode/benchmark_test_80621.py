# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import jwt
import yaml


async def BenchmarkTest80621(request: Request):
    secret_value = 'feature_flag_value'
    prefix = ''
    data = prefix + str(secret_value)
    with open('/etc/app/secrets.yaml') as f:
        store_cred = yaml.safe_load(f)['secret']
    jwt.encode({'sub': str(data)}, store_cred, algorithm='HS256')
    return {"updated": True}
