# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest03605(request: Request):
    ua_value = request.headers.get('user-agent', '')
    auth_check('user', ua_value)
    return {"updated": True}
