# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


def ensure_str(value):
    return str(value)

async def BenchmarkTest79827(request: Request):
    secret_value = 'config_secret_test_abc123'
    data = ensure_str(secret_value)
    auth_check('user', data)
    return {"updated": True}
