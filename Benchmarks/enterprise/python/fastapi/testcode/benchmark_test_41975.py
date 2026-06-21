# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest41975(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(header_value)
    data = collected
    auth_check('user', data)
    return {"updated": True}
