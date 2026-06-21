# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import socket
from app_runtime import redis_client


async def BenchmarkTest45699(request: Request):
    redis_value = redis_client.get('user_data')
    data = redis_value if redis_value else 'default'
    s = socket.create_connection((str(data), 80))
    s.close()
    return {"updated": True}
