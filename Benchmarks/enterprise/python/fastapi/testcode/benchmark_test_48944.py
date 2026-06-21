# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest48944(request: Request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    parts = str(prop_value).split(',')
    data = ','.join(parts)
    auth_check('user', data)
    return {"updated": True}
