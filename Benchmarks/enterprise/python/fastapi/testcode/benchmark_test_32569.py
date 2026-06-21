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

async def BenchmarkTest32569(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = RequestPayload(auth_header).value
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
