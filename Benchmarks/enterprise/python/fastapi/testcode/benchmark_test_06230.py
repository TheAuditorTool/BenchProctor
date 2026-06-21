# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
import json
from app_runtime import mq_client


@dataclass
class FormData:
    payload: str

async def BenchmarkTest06230(request: Request):
    msg_value = mq_client.get_message().body
    data = FormData(payload=msg_value).payload
    json.loads(data)
    return {"updated": True}
