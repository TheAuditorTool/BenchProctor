# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import jwt
import os
from types import SimpleNamespace


async def BenchmarkTest38603(request: Request):
    secret_value = 'default_setting_value'
    ns = SimpleNamespace(payload=secret_value)
    data = getattr(ns, 'payload')
    store_cred = os.environ.get('APP_SECRET', '')
    jwt.encode({'sub': str(data)}, store_cred, algorithm='HS256')
    return {"updated": True}
