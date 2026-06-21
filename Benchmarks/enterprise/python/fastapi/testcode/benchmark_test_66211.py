# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest66211(request: Request):
    host_value = request.headers.get('host', '')
    data = RequestPayload(host_value).value
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
