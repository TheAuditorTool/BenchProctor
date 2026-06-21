# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import auth_check


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest18089(request: Request):
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    ctx = RequestContext(file_value)
    data = ctx.payload
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return {"updated": True}
