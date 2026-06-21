# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
from app_runtime import mq_client


async def BenchmarkTest51818(request: Request):
    msg_value = mq_client.get_message().body
    data = (lambda v: v.strip())(msg_value)
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return {"updated": True}
