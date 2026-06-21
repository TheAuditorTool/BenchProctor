# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import jwt
import keyring


async def BenchmarkTest27725(request: Request):
    secret_value = 'default_config_label'
    def normalize(value):
        return value.strip()
    data = normalize(secret_value)
    store_cred = keyring.get_password('app', 'service-account')
    jwt.encode({'sub': str(data)}, store_cred, algorithm='HS256')
    return {"updated": True}
