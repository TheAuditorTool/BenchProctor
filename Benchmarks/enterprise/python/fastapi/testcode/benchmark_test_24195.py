# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest24195(request: Request):
    secret_value = 'config_secret_test_abc123'
    parts = str(secret_value).split(',')
    data = ','.join(parts)
    auth_check('user', data)
    return {"updated": True}
