# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from app_runtime import mq_client


async def BenchmarkTest34597(request: Request):
    msg_value = mq_client.get_message().body
    kind = 'json' if str(msg_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = msg_value
            data = parsed
        case _:
            data = msg_value
    requests.get(str(data))
    return {"updated": True}
