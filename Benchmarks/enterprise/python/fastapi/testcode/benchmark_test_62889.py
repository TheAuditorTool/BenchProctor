# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest62889(request: Request):
    host_value = request.headers.get('host', '')
    auth_check('user', host_value)
    return {"updated": True}
