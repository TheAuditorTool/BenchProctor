# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest18320(request: Request):
    secret_value = 'config_secret_test_abc123'
    prefix = ''
    data = prefix + str(secret_value)
    auth_check('user', data)
    return {"updated": True}
