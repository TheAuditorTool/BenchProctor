# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import jwt
import os


async def BenchmarkTest77336(request: Request):
    secret_value = 'default_setting_value'
    data = '%s' % str(secret_value)
    store_cred = os.environ.get('APP_SECRET', '')
    jwt.encode({'sub': str(data)}, store_cred, algorithm='HS256')
    return {"updated": True}
