# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest00967(request: Request):
    host_value = request.headers.get('host', '')
    data = host_value if host_value else 'default'
    auth_check('user', data)
    return {"updated": True}
