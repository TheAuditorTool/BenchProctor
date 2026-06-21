# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest15012(request: Request):
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    auth_check('user', secret_value)
    return {"updated": True}
