# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest06871(request: Request):
    referer_value = request.headers.get('referer', '')
    parts = str(referer_value).split(',')
    data = ','.join(parts)
    auth_check('user', data)
    return {"updated": True}
