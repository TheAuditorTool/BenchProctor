# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import jwt
import yaml


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest02980(request: Request):
    secret_value = 'app_display_name'
    ctx = RequestContext(secret_value)
    data = ctx.payload
    with open('/etc/app/secrets.yaml') as f:
        store_cred = yaml.safe_load(f)['secret']
    jwt.encode({'sub': str(data)}, store_cred, algorithm='HS256')
    return {"updated": True}
