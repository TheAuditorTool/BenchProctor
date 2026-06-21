# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


def relay_value(value):
    return value

async def BenchmarkTest72784(request: Request):
    secret_value = ['s3cr3t_key_test_xyz'][0]
    data = relay_value(secret_value)
    auth_check('user', data)
    return {"updated": True}
