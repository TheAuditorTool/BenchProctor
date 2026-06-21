# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest03727(request: Request):
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    if secret_value:
        data = secret_value
    else:
        data = ''
    auth_check('user', data)
    return {"updated": True}
