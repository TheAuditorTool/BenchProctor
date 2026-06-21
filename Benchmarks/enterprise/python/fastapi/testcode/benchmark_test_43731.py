# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest43731(request: Request):
    secret_value = 'config_secret_test_abc123'
    auth_check('user', secret_value)
    return {"updated": True}
