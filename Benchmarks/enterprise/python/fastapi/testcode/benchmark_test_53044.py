# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest53044(request: Request):
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    data = str(secret_value).replace('\x00', '')
    auth_check('user', data)
    return {"updated": True}
