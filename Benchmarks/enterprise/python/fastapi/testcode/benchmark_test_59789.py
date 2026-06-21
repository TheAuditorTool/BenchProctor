# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest59789(request: Request):
    referer_value = request.headers.get('referer', '')
    data = default_blank(referer_value)
    auth_check('user', data)
    return {"updated": True}
