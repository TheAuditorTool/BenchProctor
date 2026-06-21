# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
from app_runtime import mq_client


request_state: dict[str, str] = {}

async def BenchmarkTest01520(request: Request):
    msg_value = mq_client.get_message().body
    request_state['last_input'] = msg_value
    data = request_state['last_input']
    yaml.safe_load(data)
    return {"updated": True}
