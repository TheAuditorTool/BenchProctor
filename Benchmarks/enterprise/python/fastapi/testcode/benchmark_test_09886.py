# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


def relay_value(value):
    return value

async def BenchmarkTest09886(request: Request):
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    data = relay_value(secret_value)
    processed = data[:64]
    auth_check('user', processed)
    return {"updated": True}
