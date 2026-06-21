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

async def BenchmarkTest70095(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = RequestPayload(auth_header).value
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
