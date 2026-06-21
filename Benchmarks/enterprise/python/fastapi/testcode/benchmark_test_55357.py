# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest55357(request: Request):
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    data, _sep, _rest = str(secret_value).partition('\x00')
    auth_check('user', data)
    return {"updated": True}
