# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest46465(request: Request):
    host_value = request.headers.get('host', '')
    data = str(host_value).replace('\x00', '')
    auth_check('user', data)
    return {"updated": True}
