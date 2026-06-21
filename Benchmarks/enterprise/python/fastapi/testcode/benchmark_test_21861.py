# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import time


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest21861(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    ctx = RequestContext(env_value)
    data = ctx.payload
    if time.time() > 1000000000:
        with open('/var/uploads/' + str(data), 'wb') as fh:
            fh.write(b'data')
    return {"updated": True}
