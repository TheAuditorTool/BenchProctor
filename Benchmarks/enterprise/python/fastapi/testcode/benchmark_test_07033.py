# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest07033(request: Request):
    secret_value = ['s3cr3t_key_test_xyz'][0]
    prefix = ''
    data = prefix + str(secret_value)
    auth_check('user', data)
    return {"updated": True}
