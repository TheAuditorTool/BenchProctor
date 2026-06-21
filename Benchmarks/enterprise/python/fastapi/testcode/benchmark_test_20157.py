# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from app_runtime import mq_client


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest20157(request: Request):
    msg_value = mq_client.get_message().body
    ctx = RequestContext(msg_value)
    data = ctx.payload
    json.loads(data)
    return {"updated": True}
