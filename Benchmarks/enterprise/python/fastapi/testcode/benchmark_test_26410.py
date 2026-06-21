# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import socket


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest26410(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = RequestPayload(xml_value).value
    s = socket.create_connection((str(data), 80))
    s.close()
    return {"updated": True}
