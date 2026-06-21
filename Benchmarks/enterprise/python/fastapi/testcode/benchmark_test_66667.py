# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest66667(request: Request):
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    data = str(yaml_value).replace('\x00', '')
    auth_check('user', data)
    return {"updated": True}
