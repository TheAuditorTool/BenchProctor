# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest36252(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = f'{header_value}'
    auth_check('user', data)
    return {"updated": True}
