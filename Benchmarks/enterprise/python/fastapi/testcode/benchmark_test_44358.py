# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import socket
from app_runtime import mq_client


async def BenchmarkTest44358(request: Request):
    msg_value = mq_client.get_message().body
    kind = 'json' if str(msg_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = msg_value
            data = parsed
        case _:
            data = msg_value
    s = socket.create_connection((str(data), 80))
    s.close()
    return {"updated": True}
