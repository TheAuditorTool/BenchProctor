# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest00083(request: Request):
    origin_value = request.headers.get('origin', '')
    data = RequestPayload(origin_value).value
    subprocess.run('echo ' + str(data), shell=True)
    return {"updated": True}
