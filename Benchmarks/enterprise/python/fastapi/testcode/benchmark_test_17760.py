# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from types import SimpleNamespace
from app_runtime import auth_check


async def BenchmarkTest17760(request: Request):
    secret_value = 'default_setting_value'
    ns = SimpleNamespace(payload=secret_value)
    data = getattr(ns, 'payload')
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return {"updated": True}
