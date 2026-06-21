# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest77102(request: Request):
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    def normalize(value):
        return value.strip()
    data = normalize(yaml_value)
    auth_check('user', data)
    return {"updated": True}
