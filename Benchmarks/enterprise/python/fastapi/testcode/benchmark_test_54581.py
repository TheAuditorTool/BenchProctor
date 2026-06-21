# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from app_runtime import mq_client


async def BenchmarkTest54581(request: Request):
    msg_value = mq_client.get_message().body
    data, _sep, _rest = str(msg_value).partition('\x00')
    json.loads(data)
    return {"updated": True}
