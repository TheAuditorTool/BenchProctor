# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest72312(request: Request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    auth_check('user', prop_value)
    return {"updated": True}
