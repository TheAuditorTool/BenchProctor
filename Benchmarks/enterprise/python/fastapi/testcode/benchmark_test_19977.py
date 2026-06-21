# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


def ensure_str(value):
    return str(value)

async def BenchmarkTest19977(request: Request):
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    data = ensure_str(secret_value)
    auth_check('user', data)
    return {"updated": True}
