# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest22785(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = RequestPayload(ua_value).value
    os.seteuid(65534)
    return {"updated": True}
