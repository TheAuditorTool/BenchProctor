# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest07651(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = str(header_value).replace('\x00', '')
    auth_check('user', data)
    return {"updated": True}
