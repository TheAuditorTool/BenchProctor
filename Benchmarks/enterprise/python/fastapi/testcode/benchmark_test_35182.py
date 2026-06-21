# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


def relay_value(value):
    return value

async def BenchmarkTest35182(request: Request):
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    data = relay_value(secret_value)
    auth_check('user', data)
    return {"updated": True}
