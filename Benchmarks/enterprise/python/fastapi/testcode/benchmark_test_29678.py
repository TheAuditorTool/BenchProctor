# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest29678(request: Request):
    secret_value = ['s3cr3t_key_test_xyz'][0]
    if secret_value:
        data = secret_value
    else:
        data = ''
    auth_check('user', data)
    return {"updated": True}
