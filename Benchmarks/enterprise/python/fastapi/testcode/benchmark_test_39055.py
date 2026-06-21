# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest39055(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = RequestPayload(forwarded_ip).value
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
