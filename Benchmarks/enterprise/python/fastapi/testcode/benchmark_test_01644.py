# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest01644(request: Request):
    origin_value = request.headers.get('origin', '')
    data = f'{origin_value:.200s}'
    auth_check('user', data)
    return {"updated": True}
