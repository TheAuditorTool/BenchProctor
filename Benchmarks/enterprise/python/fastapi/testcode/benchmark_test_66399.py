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

async def BenchmarkTest66399(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = RequestPayload(raw_body).value
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
