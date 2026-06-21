# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest19125(request: Request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = ' '.join(str(config_value).split())
    auth_check('user', data)
    return {"updated": True}
