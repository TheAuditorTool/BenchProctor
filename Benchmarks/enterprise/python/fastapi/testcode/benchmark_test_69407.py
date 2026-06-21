# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import jwt
import keyring
from types import SimpleNamespace


async def BenchmarkTest69407(request: Request):
    secret_value = 'default_setting_value'
    ns = SimpleNamespace(payload=secret_value)
    data = getattr(ns, 'payload')
    store_cred = keyring.get_password('app', 'service-account')
    jwt.encode({'sub': str(data)}, store_cred, algorithm='HS256')
    return {"updated": True}
