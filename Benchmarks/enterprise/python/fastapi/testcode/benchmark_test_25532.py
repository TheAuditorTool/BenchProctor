# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest25532(request: Request):
    host_value = request.headers.get('host', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(host_value)
    data = collected
    auth_check('user', data)
    return {"updated": True}
