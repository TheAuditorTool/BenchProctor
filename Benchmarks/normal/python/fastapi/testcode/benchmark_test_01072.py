# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from app_runtime import mq_client


async def BenchmarkTest01072(request: Request):
    msg_value = mq_client.get_message().body
    def normalize(value):
        return value.strip()
    data = normalize(msg_value)
    requests.get(str(data))
    return {"updated": True}
