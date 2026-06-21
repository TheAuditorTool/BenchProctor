# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from app_runtime import mq_client


async def BenchmarkTest64602(request: Request):
    msg_value = mq_client.get_message().body
    data, _sep, _rest = str(msg_value).partition('\x00')
    requests.get(str(data))
    return {"updated": True}
