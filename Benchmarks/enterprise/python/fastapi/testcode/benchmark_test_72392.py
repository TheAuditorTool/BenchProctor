# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import jwt
import yaml


async def BenchmarkTest72392(request: Request):
    secret_value = 'default_setting_value'
    if secret_value:
        data = secret_value
    else:
        data = ''
    with open('/etc/app/secrets.yaml') as f:
        store_cred = yaml.safe_load(f)['secret']
    jwt.encode({'sub': str(data)}, store_cred, algorithm='HS256')
    return {"updated": True}
