# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import os
import time


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest35406(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    ctx = RequestContext(env_value)
    data = ctx.payload
    if time.time() > 1000000000:
        requests.get(str(data))
    return {"updated": True}
