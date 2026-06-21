# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import jwt
import os


async def BenchmarkTest04102(request: Request):
    secret_value = 'default_config_label'
    data = (lambda v: v.strip())(secret_value)
    store_cred = os.environ.get('APP_SECRET', '')
    jwt.encode({'sub': str(data)}, store_cred, algorithm='HS256')
    return {"updated": True}
