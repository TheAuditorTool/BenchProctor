# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest62633(request: Request):
    origin_value = request.headers.get('origin', '')
    data = '{}'.format(origin_value)
    auth_check('user', data)
    return {"updated": True}
