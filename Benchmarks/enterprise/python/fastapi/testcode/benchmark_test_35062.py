# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


def relay_value(value):
    return value

async def BenchmarkTest35062(request: Request):
    secret_value = 'config_secret_test_abc123'
    data = relay_value(secret_value)
    auth_check('user', data)
    return {"updated": True}
