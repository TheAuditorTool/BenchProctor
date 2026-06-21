# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from types import SimpleNamespace
from app_runtime import auth_check


async def BenchmarkTest00379(request: Request):
    secret_value = 'config_secret_test_abc123'
    ns = SimpleNamespace(payload=secret_value)
    data = getattr(ns, 'payload')
    auth_check('user', data)
    return {"updated": True}
