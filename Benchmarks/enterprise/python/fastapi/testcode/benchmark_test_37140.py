# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest37140(request: Request):
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    data = secret_value if secret_value else 'default'
    auth_check('user', data)
    return {"updated": True}
