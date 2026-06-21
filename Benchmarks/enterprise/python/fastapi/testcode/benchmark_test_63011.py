# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest63011(request: Request):
    host_value = request.headers.get('host', '')
    data = RequestPayload(host_value).value
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
