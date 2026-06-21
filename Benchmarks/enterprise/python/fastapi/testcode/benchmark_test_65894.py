# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest65894(request: Request):
    path_value = request.path_params.get('id', '')
    data = RequestPayload(path_value).value
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return {"updated": True}
