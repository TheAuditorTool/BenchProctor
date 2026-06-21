# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest01117(request: Request):
    path_value = request.path_params.get('id', '')
    ctx = RequestContext(path_value)
    data = ctx.payload
    if os.environ.get("APP_ENV", "production") != "test":
        link_path = os.path.join('/var/app/data', str(data))
        target = os.readlink(link_path)
        with open(target, 'r') as fh:
            content = fh.read()
        return content
    return {"updated": True}
