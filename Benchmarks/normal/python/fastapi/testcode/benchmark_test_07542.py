# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import socket
from app_runtime import redis_client


async def BenchmarkTest07542(request: Request):
    redis_value = redis_client.get('user_data')
    data, _sep, _rest = str(redis_value).partition('\x00')
    s = socket.create_connection((str(data), 80))
    s.close()
    return {"updated": True}
