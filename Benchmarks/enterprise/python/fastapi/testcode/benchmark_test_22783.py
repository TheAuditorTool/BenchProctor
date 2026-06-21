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

async def BenchmarkTest22783(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = RequestPayload(header_value).value
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
