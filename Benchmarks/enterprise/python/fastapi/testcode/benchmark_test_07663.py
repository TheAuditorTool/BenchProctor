# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest07663(request: Request):
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(secret_value)
    data = collected
    auth_check('user', data)
    return {"updated": True}
