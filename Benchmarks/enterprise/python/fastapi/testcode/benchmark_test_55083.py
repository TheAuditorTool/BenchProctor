# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest55083(request: Request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    if prop_value:
        data = prop_value
    else:
        data = ''
    auth_check('user', data)
    return {"updated": True}
