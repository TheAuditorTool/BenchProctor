# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
from app_runtime import redis_client


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest40690(request: Request):
    redis_value = redis_client.get('user_data')
    ctx = RequestContext(redis_value)
    data = ctx.payload
    yaml.safe_load(data)
    return {"updated": True}
