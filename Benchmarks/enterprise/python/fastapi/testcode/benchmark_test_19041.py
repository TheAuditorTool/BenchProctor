# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from app_runtime import mq_client


async def BenchmarkTest19041(request: Request):
    msg_value = mq_client.get_message().body
    data = f'{msg_value:.200s}'
    requests.get(str(data))
    return {"updated": True}
