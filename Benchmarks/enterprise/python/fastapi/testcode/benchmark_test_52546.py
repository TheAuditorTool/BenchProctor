# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import socket
from app_runtime import redis_client


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest52546(request: Request):
    redis_value = redis_client.get('user_data')
    data = RequestPayload(redis_value).value
    s = socket.create_connection((str(data), 80))
    s.close()
    return {"updated": True}
