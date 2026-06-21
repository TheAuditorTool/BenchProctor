# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest08486(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = RequestPayload(header_value).value
    subprocess.run([str(data), '--status'], shell=False)
    return {"updated": True}
