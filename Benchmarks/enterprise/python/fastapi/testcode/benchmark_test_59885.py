# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from app_runtime import mq_client


async def BenchmarkTest59885(request: Request):
    msg_value = mq_client.get_message().body
    parts = str(msg_value).split(',')
    data = ','.join(parts)
    json.loads(data)
    return {"updated": True}
