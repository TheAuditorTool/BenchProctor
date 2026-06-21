# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest29371(request: Request):
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    data = coalesce_blank(secret_value)
    auth_check('user', data)
    return {"updated": True}
