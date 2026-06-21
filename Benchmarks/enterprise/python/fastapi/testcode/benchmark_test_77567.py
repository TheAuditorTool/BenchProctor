# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest77567(request: Request):
    secret_value = 'config_secret_test_abc123'
    data = (lambda v: v.strip())(secret_value)
    auth_check('user', data)
    return {"updated": True}
