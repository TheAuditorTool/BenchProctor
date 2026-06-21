# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import socket
from app_runtime import redis_client


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest39683(request: Request):
    redis_value = redis_client.get('user_data')
    data = default_blank(redis_value)
    processed = data[:64]
    s = socket.create_connection((str(processed), 80))
    s.close()
    return {"updated": True}
