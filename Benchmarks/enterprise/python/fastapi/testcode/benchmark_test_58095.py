# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import base64
import socket
from app_runtime import mq_client


async def BenchmarkTest58095(request: Request):
    msg_value = mq_client.get_message().body
    data = base64.b64decode(msg_value).decode('utf-8', 'ignore')
    s = socket.create_connection((str(data), 80))
    s.close()
    return {"updated": True}
