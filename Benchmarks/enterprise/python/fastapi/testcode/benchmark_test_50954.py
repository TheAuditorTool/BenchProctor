# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import jwt
import os


async def BenchmarkTest50954(request: Request):
    secret_value = 'default_setting_value'
    data = ' '.join(str(secret_value).split())
    store_cred = os.environ.get('APP_SECRET', '')
    jwt.encode({'sub': str(data)}, store_cred, algorithm='HS256')
    return {"updated": True}
