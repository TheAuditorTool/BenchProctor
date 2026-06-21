# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import pickle


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest33310(request: Request):
    path_value = request.path_params.get('id', '')
    data = RequestPayload(path_value).value
    pickle.loads(data.encode('latin-1'))
    return {"updated": True}
