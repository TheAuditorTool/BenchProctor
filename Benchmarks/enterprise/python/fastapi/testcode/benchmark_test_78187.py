# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
from app_runtime import mq_client


async def BenchmarkTest78187(request: Request):
    msg_value = mq_client.get_message().body
    data = str(msg_value).replace('\x00', '')
    yaml.safe_load(data)
    return {"updated": True}
