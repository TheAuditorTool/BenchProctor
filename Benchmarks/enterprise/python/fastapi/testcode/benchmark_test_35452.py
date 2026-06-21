# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import jwt
import os


async def BenchmarkTest35452(request: Request):
    secret_value = 'app_display_name'
    data = str(secret_value).replace('\x00', '')
    store_cred = os.environ.get('APP_SECRET', '')
    jwt.encode({'sub': str(data)}, store_cred, algorithm='HS256')
    return {"updated": True}
