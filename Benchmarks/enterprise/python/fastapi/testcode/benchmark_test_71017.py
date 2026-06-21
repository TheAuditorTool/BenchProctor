# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest71017(request: Request):
    secret_value = 'config_secret_test_abc123'
    data = str(secret_value).replace('\x00', '')
    auth_check('user', data)
    return {"updated": True}
