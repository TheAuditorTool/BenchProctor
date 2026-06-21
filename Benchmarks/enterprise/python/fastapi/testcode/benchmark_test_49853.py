# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest49853(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = default_blank(header_value)
    auth_check('user', data)
    return {"updated": True}
