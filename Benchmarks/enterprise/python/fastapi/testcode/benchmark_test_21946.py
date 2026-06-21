# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest21946(request: Request):
    path_value = request.path_params.get('id', '')
    data = RequestPayload(path_value).value
    os.setuid(int(str(data)) if str(data).isdigit() else 0)
    return {"updated": True}
