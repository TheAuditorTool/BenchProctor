# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest34685(request: Request):
    referer_value = request.headers.get('referer', '')
    data = f'{referer_value:.200s}'
    auth_check('user', data)
    return {"updated": True}
