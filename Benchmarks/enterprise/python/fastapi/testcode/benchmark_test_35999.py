# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest35999(request: Request):
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(yaml_value)
    data = collected
    auth_check('user', data)
    return {"updated": True}
