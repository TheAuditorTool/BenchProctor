# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest14084(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = ' '.join(str(header_value).split())
    auth_check('user', data)
    return {"updated": True}
