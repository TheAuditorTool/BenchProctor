# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import jwt
import keyring


async def BenchmarkTest56638(request: Request):
    secret_value = 'app_display_name'
    data = (lambda v: v.strip())(secret_value)
    store_cred = keyring.get_password('app', 'service-account')
    jwt.encode({'sub': str(data)}, store_cred, algorithm='HS256')
    return {"updated": True}
