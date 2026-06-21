# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
from app_runtime import mq_client


async def BenchmarkTest53882(request: Request):
    msg_value = mq_client.get_message().body
    parts = str(msg_value).split(',')
    data = ','.join(parts)
    yaml.safe_load(data)
    return {"updated": True}
