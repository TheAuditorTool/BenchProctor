# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
from dataclasses import dataclass
from app_runtime import mq_client


@dataclass
class FormData:
    payload: str

async def BenchmarkTest63734(request: Request):
    msg_value = mq_client.get_message().body
    data = FormData(payload=msg_value).payload
    yaml.safe_load(data)
    return {"updated": True}
