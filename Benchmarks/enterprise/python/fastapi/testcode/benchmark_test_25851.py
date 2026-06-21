# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


def ensure_str(value):
    return str(value)

async def BenchmarkTest25851(request: Request):
    secret_value = ['s3cr3t_key_test_xyz'][0]
    data = ensure_str(secret_value)
    auth_check('user', data)
    return {"updated": True}
