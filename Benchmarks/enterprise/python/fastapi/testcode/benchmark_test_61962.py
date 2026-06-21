# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest61962(request: Request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    def normalize(value):
        return value.strip()
    data = normalize(prop_value)
    auth_check('user', data)
    return {"updated": True}
