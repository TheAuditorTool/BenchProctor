# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest33277(request: Request):
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    data, _sep, _rest = str(yaml_value).partition('\x00')
    auth_check('user', data)
    return {"updated": True}
