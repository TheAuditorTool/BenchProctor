# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from app_runtime import mq_client


async def BenchmarkTest06434(request: Request):
    msg_value = mq_client.get_message().body
    data = '{}'.format(msg_value)
    requests.get(str(data))
    return {"updated": True}
