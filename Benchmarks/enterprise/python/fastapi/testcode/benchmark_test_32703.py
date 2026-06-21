# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest32703(request: Request):
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    data = ' '.join(str(secret_value).split())
    auth_check('user', data)
    return {"updated": True}
