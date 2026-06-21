# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest48517(request: Request):
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    data = coalesce_blank(secret_value)
    auth_check('user', data)
    return {"updated": True}
