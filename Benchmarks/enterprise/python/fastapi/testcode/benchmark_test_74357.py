# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
from app_runtime import mq_client


async def BenchmarkTest74357(request: Request):
    msg_value = mq_client.get_message().body
    data, _sep, _rest = str(msg_value).partition('\x00')
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return {"updated": True}
