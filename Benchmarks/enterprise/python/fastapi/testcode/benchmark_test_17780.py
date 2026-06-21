# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


def to_text(value):
    return str(value).strip()

async def BenchmarkTest17780(request: Request):
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    data = to_text(secret_value)
    processed = data[:64]
    auth_check('user', processed)
    return {"updated": True}
