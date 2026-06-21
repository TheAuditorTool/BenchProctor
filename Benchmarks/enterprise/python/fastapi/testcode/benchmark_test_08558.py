# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest08558(request: Request):
    secret_value = ['s3cr3t_key_test_xyz'][0]
    data = f'{secret_value:.200s}'
    auth_check('user', data)
    return {"updated": True}
