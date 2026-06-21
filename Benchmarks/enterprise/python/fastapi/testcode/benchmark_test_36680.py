# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest36680(request: Request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(prop_value)
    data = collected
    auth_check('user', data)
    return {"updated": True}
