# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest71541(request: Request):
    referer_value = request.headers.get('referer', '')
    data = f'{referer_value}'
    auth_check('user', data)
    return {"updated": True}
