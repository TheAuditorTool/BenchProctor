# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest75823(request: Request):
    secret_value = 'config_secret_test_abc123'
    data = coalesce_blank(secret_value)
    auth_check('user', data)
    return {"updated": True}
