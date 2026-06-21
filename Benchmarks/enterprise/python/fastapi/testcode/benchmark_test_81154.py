# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import jwt
import keyring


async def BenchmarkTest81154(request: Request):
    secret_value = 'app_display_name'
    data = f'{secret_value:.200s}'
    store_cred = keyring.get_password('app', 'service-account')
    jwt.encode({'sub': str(data)}, store_cred, algorithm='HS256')
    return {"updated": True}
