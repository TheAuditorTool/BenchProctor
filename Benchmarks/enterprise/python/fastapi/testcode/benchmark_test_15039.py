# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest15039(request: Request):
    path_value = request.path_params.get('id', '')
    data = RequestPayload(path_value).value
    subprocess.run('echo ' + str(data), shell=True)
    return {"updated": True}
