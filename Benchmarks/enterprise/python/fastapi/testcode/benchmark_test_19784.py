# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest19784(request: Request):
    secret_value = ['s3cr3t_key_test_xyz'][0]
    auth_check('user', secret_value)
    return {"updated": True}
