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

async def BenchmarkTest57246(request: Request):
    referer_value = request.headers.get('referer', '')
    data = RequestPayload(referer_value).value
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
