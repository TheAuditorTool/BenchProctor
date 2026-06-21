# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import socket
from app_runtime import mq_client


async def BenchmarkTest23250(request: Request):
    msg_value = mq_client.get_message().body
    data = msg_value.decode('utf-8', 'ignore') if isinstance(msg_value, bytes) else msg_value
    s = socket.create_connection((str(data), 80))
    s.close()
    return {"updated": True}
