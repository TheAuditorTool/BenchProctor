# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest39345(request: Request):
    referer_value = request.headers.get('referer', '')
    auth_check('user', referer_value)
    return {"updated": True}
