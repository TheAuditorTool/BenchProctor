# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest44756(request: Request):
    host_value = request.headers.get('host', '')
    data = '{}'.format(host_value)
    auth_check('user', data)
    return {"updated": True}
