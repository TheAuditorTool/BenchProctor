# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest55517(request: Request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    auth_check('user', config_value)
    return {"updated": True}
