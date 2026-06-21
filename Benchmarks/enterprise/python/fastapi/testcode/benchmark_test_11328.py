# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest11328(request: Request):
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    ctx = RequestContext(yaml_value)
    data = ctx.payload
    auth_check('user', data)
    return {"updated": True}
