# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import jwt
import os
import json


async def BenchmarkTest04827(request: Request):
    secret_value = 'default_config_label'
    try:
        data = json.loads(secret_value).get('value', secret_value)
    except (json.JSONDecodeError, AttributeError):
        data = secret_value
    store_cred = os.environ.get('APP_SECRET', '')
    jwt.encode({'sub': str(data)}, store_cred, algorithm='HS256')
    return {"updated": True}
