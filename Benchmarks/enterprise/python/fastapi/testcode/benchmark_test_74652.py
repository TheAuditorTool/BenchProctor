# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import socket


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest74652(request: Request):
    host_value = request.headers.get('host', '')
    data = RequestPayload(host_value).value
    s = socket.create_connection((str(data), 80))
    s.close()
    return {"updated": True}
