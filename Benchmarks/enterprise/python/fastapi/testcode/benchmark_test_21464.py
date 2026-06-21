# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest21464(request: Request):
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    data = '%s' % str(secret_value)
    auth_check('user', data)
    return {"updated": True}
